import json
import os
from base64 import b64encode
from pathlib import Path

import requests
from dotenv import load_dotenv, find_dotenv, set_key
from nacl import encoding, public
from datetime import datetime, date, timedelta, timezone

METERS_TO_MILES = 1 / 1609.344
UNI_LAP_MILES = 0.8 # distance of one lap around the block
# scripts/strava.py -> repo root -> src/data/strava_stats.json
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "src" / "data" / "strava_stats.json"

## Strava API authentication documentation
# https://appsforstrava.com/developers/authentication/


def refresh_access_token(client_id, client_secret, refresh_token):
    """Use old refresh token to get access token and new refresh token
    for next refresh"""
    response = requests.post(
        "https://www.strava.com/oauth/token",
        json={
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token"
        })
    response.raise_for_status()
    return response.json()

def save_tokens(tokens, dotenv_path):
    """Persist rotated tokens. Strava issues a new refresh token on every
    refresh and invalidates old token, so both must be saved. Routes to
    GitHub secrets when running in Actions, otherwise to local .env."""
    if os.environ.get("GITHUB_ACTIONS") == "true":
        update_github_secrets({
            "ACCESS_TOKEN": tokens["access_token"],
            "REFRESH_TOKEN": tokens["refresh_token"],
        })
    else:
        set_key(dotenv_path, "ACCESS_TOKEN", tokens["access_token"])
        set_key(dotenv_path, "REFRESH_TOKEN", tokens["refresh_token"])

def _encrypt_secret(public_key, secret_value):
    """Encrypt a value with the repo's public key
    Secrets must be encrypted before pushed"""
    pk = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(pk)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return b64encode(encrypted).decode("utf-8")

def update_github_secrets(secrets):
    """Update repo secrets via github API"""
    repo = os.environ["GITHUB_REPOSITORY"]
    api = f"https://api.github.com/repos/{repo}/actions/secrets"
    headers = {
        "Authorization": f"Bearer {os.environ['GH_PAT']}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    # Fetch the repo public key, required to encrypt secrets
    key_resp = requests.get(f"{api}/public-key", headers=headers)
    key_resp.raise_for_status()
    pubkey = key_resp.json()

    for name, value in secrets.items():
        resp = requests.put(
            f"{api}/{name}",
            headers=headers,
            json={
                "encrypted_value": _encrypt_secret(pubkey["key"], value),
                "key_id": pubkey["key_id"],
            },
        )
        resp.raise_for_status()

def get_activities(access_token, per_page=200):
    response = requests.get(
        'https://www.strava.com/api/v3/athlete/activities',
        headers={'Authorization': f'Bearer {access_token}'},
        params={'per_page': per_page}
    )
    response.raise_for_status()
    return response.json()

def get_run_date(activity):
    """Local date of the activity/run"""
    return date.fromisoformat(activity["start_date_local"][:10])

def compute_streak(runs, base_date):
    """Compute streak of consecutive runs
    Starts at base_date and walks backwards through dates of each run"""
    run_dates = {get_run_date(a) for a in runs}
    day = base_date
    streak = 0
    while day in run_dates:
        streak += 1
        day -= timedelta(days=1)
    return streak

def miles_last_week(runs, base_date):
    """Total mileage run on the base date and 6 days preceding it (last week)"""
    cutoff = base_date - timedelta(days=6)
    last_week_meters = sum(
        a["distance"] for a in runs 
        if cutoff <= get_run_date(a) <= base_date
    )
    return last_week_meters * METERS_TO_MILES

def uni_laps_last_week(runs, base_date):
    """Uni laps on the base date and 6 days preceding it (last week)
    Uni runs have 'Uni' prefix, one activity may hold several uni laps
    Laps calculated by dividing distance run by distance of a uni lap, rounded to int
    """
    cutoff = base_date - timedelta(days=6)
    uni_meters = sum(
        a["distance"] for a in runs
        if cutoff <= get_run_date(a) <= base_date and (a.get("name") or "").startswith("Uni")
    )
    return round(uni_meters * METERS_TO_MILES / UNI_LAP_MILES)

def main():
    # Load .env into the environment when run locally
    # In github actions the workflow injects the same vars from github secrets
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)
    
    access_token = os.environ["ACCESS_TOKEN"]
    try:
        activities = get_activities(access_token)
        print("Access token still valid!")
    except requests.HTTPError as e:
        if e.response.status_code != 401:
            raise  # not an authorization error
        print("Access token expired, refreshing...")
        tokens = refresh_access_token(os.environ["STRAVA_CLIENT_ID"],
                                      os.environ["STRAVA_CLIENT_SECRET"],
                                      os.environ["REFRESH_TOKEN"])
        save_tokens(tokens, dotenv_path)
        access_token = tokens["access_token"]
        activities = get_activities(access_token)

    print(f"Found {len(activities)} activities")
    
    runs = [a for a in activities if a.get("type") == "Run"]

    # Github Action is scheduled to run overnight for pacific timezone
    # If there was no run the day before, the streak should break
    # So make the "base date" the day before current UTC date
    # base_date becomes the landmark for computing statistics
    base_date = datetime.now(timezone.utc).date() - timedelta(days=1)

    stats = {
        "streak": compute_streak(runs, base_date),
        "milesLastWeek": round(miles_last_week(runs, base_date), 1),
        "uniLapsLastWeek": uni_laps_last_week(runs, base_date),
        "updatedAt": base_date.isoformat(),
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(stats, indent=2))
    print(f"Wrote {OUTPUT_PATH}: {stats}")

if __name__ == "__main__":
    main()