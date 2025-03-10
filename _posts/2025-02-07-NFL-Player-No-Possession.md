---
layout: post
author: Maxwell McNeal
title: Who was the best NFL player without a possession?
excerpt: The best football players with no football
---
On December 14th, 2024, Travis Hunter won the Heisman Trophy, the award for the best player in college football that year. On April 24th, at the 2025 NFL draft, we are going to hear his name get called, and watch the most dynamic two-way player since Deion Sanders, his college coach, get drafted. His skills on both sides of the ball make him an absolute outlier in modern football.

Most NFL players live on either offense or defense. But, it wasn't always this way. The one-platoon system, where the same players played both offense and defense, was the standard in the NFL until 1943 due to rules requiring players to sit for the rest of the half or quarter if they came out of the game. With the implementation of unlimited substitutions in 1943, teams rapidly realized how beneficial it was to have specialized players for offense and defense.

Now, football has evolved into a game of hyper-specialization. On offense, only specific players are allowed to catch a forward pass, lest they suffer an illegal touching penalty. On defense, linebackers are frequently pulled off the field in favor of another defensive back to better defend the offensive personnel. Each position has a strictly defined set of rules and responsibilites. And, unlike most other sports, there is a group of players, linemen, who are never intended to touch the football. Fans, broadcasters, and fellow players alike celebrate when big men get the football and start [rumbling](https://www.youtube.com/watch?v=-3N2hLorjns) [down](https://www.youtube.com/watch?v=uCa3YMd7f88) [the](https://www.youtube.com/watch?v=Jiu52DN8vYA) [field](https://www.youtube.com/watch?v=AGI4wbgyyoQ), in part because of how rare and almost unnatural it seems. This compelled me to ask the question: Who has had the best career in the NFL without ever holding the football?

## The Rules
First, let me clarify what I mean by "holding the football". I am specifically interested in the best NFL player who never had posession of the football during any of their NFL games. This means they cannot have any passing attempts, rushing attempts, receptions, or yards of any kind, including special teams. Also, they cannot have recovered any fumbles or picked off any passes. As for determining the "best" player out of those who remain, I think using games played as a proxy is helpful. A player who played 10 seasons but never got the ball obviously contributed in many other ways, otherwise they would be out of the league. Statistics won't tell the whole story, especially given offensive lineman's lack of counting stats in a box score, so I will individually investigate the top players after I get my short list of contenders.

Before I dive into the actual data, let's mentally narrow down who is in the running for this award. This immediately disqualifies all offensive players who got the ball, eliminating all quarterbacks, runningbacks, receivers, and tight ends (if they caught a passes). This leaves only offensive linemen and tight ends who never caught a pass, which basically means only offensive linemen. Of course, only offensive linemenwho haven't falled on a fumble either. On the defensive side, it doesn't technically outright eliminate any entire positions. However, it seems like it would eliminate defensive backs and most linebackers. It seems hard to imagine a player in the secondary with no interceptions having a better overall career than a defensive lineman with no fumble recoveries. Lastly, kickers and punters are not eligible. Punters clearly possess the ball prior to punting it, and while it's more gray with kickers, it feels against the spirit of my question.

## The Data
I will be using the dataset outlined in my [last post](https://www.maxwellmcneal.com/2025/01/29/PFR-Scraper.html). It contains the careers statistics of all NFL players in history, scraped from the Pro Football Reference website.

First, I'm going to add some helper columns and combine regular and postseason games played and starts for easier viewing.
```python
player_stats = pd.read_csv('player_stats.csv')

player_stats['career_length'] = player_stats['career_end'] - player_stats['career_begin'] + 1
player_stats['games'] = player_stats['games_reg'] + player_stats['games_post']
player_stats['games_started'] = player_stats['games_started_reg'] + player_stats['games_started_post']
player_stats['start_pct'] = player_stats['games_started'] / player_stats['games']
```
I want to cut all players with any possessions, meaning pass attempts, rush attempts, receptions, kick returns, or punt returns, as well as any interceptions or fumbles recovered, in either the regular season or postseason.
```python
players = player_stats[
    (player_stats['position'] != 'K') &
    (player_stats['position'] != 'P') &
    (player_stats['pass_att_reg'] == 0) &
    (player_stats['pass_att_post'] == 0) &
    (player_stats['rush_att_reg'] == 0) &
    (player_stats['rush_att_post'] == 0) &
    (player_stats['rec_reg'] == 0) &
    (player_stats['rec_post'] == 0) &
    (player_stats['def_int_reg'] == 0) &
    (player_stats['def_int_post'] == 0) &
    (player_stats['fumbles_rec_reg'] == 0) &
    (player_stats['fumbles_rec_post'] == 0) &
    (player_stats['punt_ret_reg'] == 0) &
    (player_stats['punt_ret_post'] == 0) &
    (player_stats['kick_ret_reg'] == 0) &
    (player_stats['kick_ret_post'] == 0)
]
```
Finally, I want to sort the resulting players by total games played and display the relevant columns for the top 10 players.
```python
players = players.sort_values(by='games', ascending=False)
players_display = players[['name', 'position', 'career_length', 'games', 'games_started', 'start_pct']]
players_display.head(10)
```

|       | name            | position   |   career_length |   games |   games_started |   start_pct |
|------:|:----------------|:-----------|----------------:|--------:|----------------:|------------:|
| 12226 | J.J. Jansen     | C          |              16 |     267 |               0 |   0         |
| 17794 | Don Muhlbach    | C          |              17 |     263 |               0 |   0         |
| 10661 | Dale Hellestrae | T-G-C      |              17 |     226 |               4 |   0.0176991 |
| 23218 | Justin Snow     | TE         |              13 |     218 |               0 |   0         |
| 10176 | Clark Harris    | TE         |              15 |     216 |               0 |   0         |
| 10229 | Josh Harris     | LS         |              13 |     216 |               0 |   0         |
|  6469 | Jon Dorenbos    | C          |              14 |     209 |               0 |   0         |
| 16718 | Jake McQuaide   | LS         |              14 |     207 |               0 |   0         |
| 17638 | Mike Morris     | C-G        |              13 |     198 |               0 |   0         |
|  3819 | Joe Cardona     | LS         |              10 |     173 |               0 |   0         |

On first glance, this seems promising. A mix of offensive linemen and tight ends, with a couple long snappers. But looking closer, it's odd that almost none of the top 10 have started a game, except Dale Hellestrae, who seems to be an gadget offensive linemen. Looking at J.J. Jansen's Pro Football Reference [page](https://www.pro-football-reference.com/players/J/JansJ.00.htm), we find the devil is in the details. Despite being listed as a center in his header, for each season he has played, he is actually been listed as a long snapper. Everyone else on this list, they're all long snappers as well. I've essentially compiled a list of long snappers who haven't done anything besides long snapping, sorted by games played. Not at all what I wanted. 

Looking further down the list, it seems like the first player who isn't a long snapper on this list is [Tim Ruddy](https://www.pro-football-reference.com/players/R/RuddTi20.htm). A legitimate center, he played 156 games across 10 years, starting 140 of them, with a Pro Bowl selection in 2000. However, as a center, he has 3 fumbles credited to him due to bad snaps. You can watch one of them [here](https://youtu.be/eIYj9G57P20?t=576). This one specifically looks like it's all on Ruddy to me. When he snaps the ball, Marino is looking at the sideline, clearly not expecting the snap. I think for the sake of this question, fumbling the ball means necessitates that you had possession of it, thus eliminating all centers and long snappers seen before. [^1]

The next real offensive lineman seems to be [Rudy Comstock](https://www.pro-football-reference.com/players/C/ComsRu20.htm). A guard and tackle, he had a 11 year career that spanned 152 games and 127 starts. However, he played in the 1920s and 30s. Individual stat keeping and box scores don't span back that far, so we have no real way of telling if Comstock ever possessed the football on the field or not.

The first defensive player on the list is [Ramon Humber](https://www.pro-football-reference.com/players/H/HumbRa00.htm). A linebacker who played 148 games and started 30 across 10 years. He racked up 312 combined tackles and 4.5 sacks. But looking at his snaps counts, which PFR has tracked since 2012, he struggled to consistently see the field on defense, with the majority of his snaps coming on special teams. A good career, for sure, but not the caliber of player I thought I would arrive at. And honestly, not a satisfying answer to me. 

## Reconsidering
What if I revise my original question? I thought I was going to find some of the best linemen across NFL history, not players from the 1920s and an average defensive starter. Now that I've seen just how strict my requirements were before, I want to see what kinds of players I get if loosen the standards to see if I can satisfyingly answer this odd question about football players with no football. I think the "no fumble recoveries" requirement is what's eliminating many of the great linemen, both offensive and defensive. Fumble recoveries are not exactly a skill, they're more of a "right place, right time" thing. And the more snaps you're on the field for, the more fumbles you'll witness, and the more chances you have to dive on a loose ball at least once in your career. I need to bend the rules here to allow for players to have recovered some fumbles. But, I still want to make sure these players don't have any fumble returns, and definitely no scoop and scores. I'm going to rerun this list, but change the no fumble recoveries to no fumble recovery yards. To eliminate all the long snappers, I'm going to also set a requirement that a player's percentage of games started is greater than 50%. Lastly, I'm going to add the requirement of no fumbles, given that we established that a player who fumbles must necessarily have had posession earlier.

```python
player_stats['position_list'] = player_stats['position'].str.split('-')

players = player_stats[
    (player_stats['position'] != 'K') &
    (player_stats['position'] != 'P') &
    (player_stats['pass_att_reg'] == 0) &
    (player_stats['pass_att_post'] == 0) &
    (player_stats['rush_att_reg'] == 0) &
    (player_stats['rush_att_post'] == 0) &
    (player_stats['rec_reg'] == 0) &
    (player_stats['rec_post'] == 0) &
    (player_stats['def_int_reg'] == 0) &
    (player_stats['def_int_post'] == 0) &
    (player_stats['fumbles_reg'] == 0) &
    (player_stats['fumbles_post'] == 0) &
    (player_stats['fumbles_rec_yds_reg'] <= 0) &
    (player_stats['fumbles_rec_yds_post'] <= 0) &
    (player_stats['punt_ret_reg'] == 0) &
    (player_stats['punt_ret_post'] == 0) &
    (player_stats['kick_ret_reg'] == 0) &
    (player_stats['kick_ret_post'] == 0) & 
    (player_stats['start_pct'] > 0.5)
]
players = players[players['position_list'].apply(lambda x: 'C' not in x)]

players = players.sort_values(by='games', ascending=False)
players_display = players[['name', 'position', 'career_length', 'games', 'games_started', 'start_pct']]
players_display.head(10)
```

|       | name          | position   |   career_length |   games |   games_started |   start_pct |
|------:|:--------------|:-----------|----------------:|--------:|----------------:|------------:|
|  3039 | Ray Brown     | G-T        |              20 |     274 |             216 |    0.788321 |
| 13549 | Mike Kenn     | T          |              17 |     257 |             257 |    1        |
| 20871 | Jim Ritcher   | G          |              16 |     238 |             180 |    0.756303 |
| 17394 | Max Montoya   | G          |              16 |     234 |             206 |    0.880342 |
|  2928 | Duane Brown   | T          |              16 |     229 |             227 |    0.991266 |
| 23654 | Todd Steussie | T          |              14 |     228 |             199 |    0.872807 |
|  8940 | Kevin Gogan   | G-T        |              14 |     227 |             189 |    0.832599 |
| 19611 | Ryan Pickett  | DT         |              14 |     224 |             198 |    0.883929 |
|  8438 | Wayne Gandy   | T          |              15 |     223 |             209 |    0.93722  |
|  7420 | Alan Faneca   | G-T        |              13 |     220 |             215 |    0.977273 |

That's more like it. The list now contains excellent offensive linemen with long careers, which is to be expected. As stated previously, offensive lineman careers are challenging to evaluate solely with statistics, especially for older players. Career length or games played are not the right way to rank them. It merely helps us narrow down the candidates. The list above is the top 10 remaining players by games played. Which seems good, but if you look just outside the top 10, we find notable players like Larry Allen. Only 10 or so games played separate him from our top 10. It seems wrong to choose a game cutoff to determine our best player. Instead, I'm going to institute a requirement of at least a 10 year long career, then evaluate the entire list. The full table of eligible players is long, so I've hidden it in a collapsible section below. Click the header to see the full list.

<details>
<summary> Full Player List </summary>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>name</th>
      <th>position</th>
      <th>career_length</th>
      <th>games</th>
      <th>games_started</th>
      <th>start_pct</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ray Brown</td>
      <td>G-T</td>
      <td>20</td>
      <td>274</td>
      <td>216</td>
      <td>0.788321</td>
    </tr>
    <tr>
      <td>Mike Kenn</td>
      <td>T</td>
      <td>17</td>
      <td>257</td>
      <td>257</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>Jim Ritcher</td>
      <td>G</td>
      <td>16</td>
      <td>238</td>
      <td>180</td>
      <td>0.756303</td>
    </tr>
    <tr>
      <td>Max Montoya</td>
      <td>G</td>
      <td>16</td>
      <td>234</td>
      <td>206</td>
      <td>0.880342</td>
    </tr>
    <tr>
      <td>Duane Brown</td>
      <td>T</td>
      <td>16</td>
      <td>229</td>
      <td>227</td>
      <td>0.991266</td>
    </tr>
    <tr>
      <td>Todd Steussie</td>
      <td>T</td>
      <td>14</td>
      <td>228</td>
      <td>199</td>
      <td>0.872807</td>
    </tr>
    <tr>
      <td>Kevin Gogan</td>
      <td>G-T</td>
      <td>14</td>
      <td>227</td>
      <td>189</td>
      <td>0.832599</td>
    </tr>
    <tr>
      <td>Ryan Pickett</td>
      <td>DT</td>
      <td>14</td>
      <td>224</td>
      <td>198</td>
      <td>0.883929</td>
    </tr>
    <tr>
      <td>Wayne Gandy</td>
      <td>T</td>
      <td>15</td>
      <td>223</td>
      <td>209</td>
      <td>0.937220</td>
    </tr>
    <tr>
      <td>Alan Faneca</td>
      <td>G-T</td>
      <td>13</td>
      <td>220</td>
      <td>215</td>
      <td>0.977273</td>
    </tr>
    <tr>
      <td>Steve Wisniewski</td>
      <td>G</td>
      <td>13</td>
      <td>215</td>
      <td>215</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>Larry Allen</td>
      <td>G-T</td>
      <td>14</td>
      <td>213</td>
      <td>207</td>
      <td>0.971831</td>
    </tr>
    <tr>
      <td>Len Rohde</td>
      <td>T</td>
      <td>15</td>
      <td>213</td>
      <td>184</td>
      <td>0.863850</td>
    </tr>
    <tr>
      <td>Will Wolford</td>
      <td>T-G</td>
      <td>13</td>
      <td>211</td>
      <td>211</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>William Roberts</td>
      <td>G-T</td>
      <td>14</td>
      <td>209</td>
      <td>165</td>
      <td>0.789474</td>
    </tr>
    <tr>
      <td>Flozell Adams</td>
      <td>T-G-TE</td>
      <td>13</td>
      <td>208</td>
      <td>204</td>
      <td>0.980769</td>
    </tr>
    <tr>
      <td>Henry Lawrence</td>
      <td>T-G</td>
      <td>13</td>
      <td>207</td>
      <td>161</td>
      <td>0.777778</td>
    </tr>
    <tr>
      <td>Kevin Donnalley</td>
      <td>G-T</td>
      <td>13</td>
      <td>207</td>
      <td>153</td>
      <td>0.739130</td>
    </tr>
    <tr>
      <td>Russ Washington</td>
      <td>T-DT</td>
      <td>15</td>
      <td>205</td>
      <td>201</td>
      <td>0.980488</td>
    </tr>
    <tr>
      <td>Harry Swayne</td>
      <td>T-DE</td>
      <td>15</td>
      <td>204</td>
      <td>126</td>
      <td>0.617647</td>
    </tr>
    <tr>
      <td>Brad Hopkins</td>
      <td>T</td>
      <td>13</td>
      <td>204</td>
      <td>198</td>
      <td>0.970588</td>
    </tr>
    <tr>
      <td>Winston Hill</td>
      <td>T</td>
      <td>15</td>
      <td>201</td>
      <td>185</td>
      <td>0.920398</td>
    </tr>
    <tr>
      <td>Willie Anderson</td>
      <td>T</td>
      <td>13</td>
      <td>199</td>
      <td>188</td>
      <td>0.944724</td>
    </tr>
    <tr>
      <td>Keith Van Horne</td>
      <td>T</td>
      <td>13</td>
      <td>198</td>
      <td>181</td>
      <td>0.914141</td>
    </tr>
    <tr>
      <td>Tony Jones</td>
      <td>T-G</td>
      <td>13</td>
      <td>197</td>
      <td>186</td>
      <td>0.944162</td>
    </tr>
    <tr>
      <td>Steve Wallace</td>
      <td>T-G</td>
      <td>12</td>
      <td>197</td>
      <td>142</td>
      <td>0.720812</td>
    </tr>
    <tr>
      <td>Richmond Webb</td>
      <td>T</td>
      <td>13</td>
      <td>197</td>
      <td>196</td>
      <td>0.994924</td>
    </tr>
    <tr>
      <td>Joe Devlin</td>
      <td>T-G</td>
      <td>14</td>
      <td>197</td>
      <td>185</td>
      <td>0.939086</td>
    </tr>
    <tr>
      <td>Bob Young</td>
      <td>G-DE-DT</td>
      <td>16</td>
      <td>197</td>
      <td>152</td>
      <td>0.771574</td>
    </tr>
    <tr>
      <td>Charles Mann</td>
      <td>DE</td>
      <td>12</td>
      <td>196</td>
      <td>159</td>
      <td>0.811224</td>
    </tr>
    <tr>
      <td>Paul Howard</td>
      <td>G</td>
      <td>14</td>
      <td>195</td>
      <td>155</td>
      <td>0.794872</td>
    </tr>
    <tr>
      <td>Larry Little</td>
      <td>G-T</td>
      <td>14</td>
      <td>195</td>
      <td>167</td>
      <td>0.856410</td>
    </tr>
    <tr>
      <td>Dave Lutz</td>
      <td>T-G</td>
      <td>13</td>
      <td>195</td>
      <td>179</td>
      <td>0.917949</td>
    </tr>
    <tr>
      <td>Glenn Parker</td>
      <td>G-T</td>
      <td>12</td>
      <td>193</td>
      <td>157</td>
      <td>0.813472</td>
    </tr>
    <tr>
      <td>Jeff Backus</td>
      <td>T</td>
      <td>12</td>
      <td>192</td>
      <td>192</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>Brian Waters</td>
      <td>G</td>
      <td>14</td>
      <td>192</td>
      <td>176</td>
      <td>0.916667</td>
    </tr>
    <tr>
      <td>Willie Roaf</td>
      <td>T</td>
      <td>13</td>
      <td>192</td>
      <td>192</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>Tom Neville</td>
      <td>T</td>
      <td>15</td>
      <td>192</td>
      <td>150</td>
      <td>0.781250</td>
    </tr>
    <tr>
      <td>Fred Miller</td>
      <td>T-G</td>
      <td>13</td>
      <td>192</td>
      <td>164</td>
      <td>0.854167</td>
    </tr>
    <tr>
      <td>Joe Jacoby</td>
      <td>T-G</td>
      <td>13</td>
      <td>191</td>
      <td>167</td>
      <td>0.874346</td>
    </tr>
    <tr>
      <td>Tra Thomas</td>
      <td>T</td>
      <td>12</td>
      <td>191</td>
      <td>185</td>
      <td>0.968586</td>
    </tr>
    <tr>
      <td>Marshal Yanda</td>
      <td>G</td>
      <td>13</td>
      <td>191</td>
      <td>180</td>
      <td>0.942408</td>
    </tr>
    <tr>
      <td>Bryant McKinnie</td>
      <td>T</td>
      <td>12</td>
      <td>190</td>
      <td>173</td>
      <td>0.910526</td>
    </tr>
    <tr>
      <td>Barney Chavous</td>
      <td>DE-DT</td>
      <td>13</td>
      <td>190</td>
      <td>185</td>
      <td>0.973684</td>
    </tr>
    <tr>
      <td>Walter Jones</td>
      <td>T</td>
      <td>12</td>
      <td>190</td>
      <td>190</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>Dave Szott</td>
      <td>G</td>
      <td>14</td>
      <td>189</td>
      <td>183</td>
      <td>0.968254</td>
    </tr>
    <tr>
      <td>John Alt</td>
      <td>T</td>
      <td>13</td>
      <td>189</td>
      <td>158</td>
      <td>0.835979</td>
    </tr>
    <tr>
      <td>Joe DeLamielleure</td>
      <td>G</td>
      <td>13</td>
      <td>188</td>
      <td>178</td>
      <td>0.946809</td>
    </tr>
    <tr>
      <td>Andy Heck</td>
      <td>T-G</td>
      <td>12</td>
      <td>188</td>
      <td>167</td>
      <td>0.888298</td>
    </tr>
    <tr>
      <td>Norm Evans</td>
      <td>T</td>
      <td>14</td>
      <td>188</td>
      <td>166</td>
      <td>0.882979</td>
    </tr>
    <tr>
      <td>Rodger Saffold</td>
      <td>T</td>
      <td>13</td>
      <td>187</td>
      <td>184</td>
      <td>0.983957</td>
    </tr>
    <tr>
      <td>Renaldo Wynn</td>
      <td>DE-DT</td>
      <td>13</td>
      <td>187</td>
      <td>132</td>
      <td>0.705882</td>
    </tr>
    <tr>
      <td>Howard Ballard</td>
      <td>T</td>
      <td>11</td>
      <td>186</td>
      <td>168</td>
      <td>0.903226</td>
    </tr>
    <tr>
      <td>Paul Gruber</td>
      <td>T</td>
      <td>12</td>
      <td>185</td>
      <td>185</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>Ed Budde</td>
      <td>G</td>
      <td>14</td>
      <td>184</td>
      <td>168</td>
      <td>0.913043</td>
    </tr>
    <tr>
      <td>John Williams</td>
      <td>T-G-DE</td>
      <td>12</td>
      <td>184</td>
      <td>144</td>
      <td>0.782609</td>
    </tr>
    <tr>
      <td>Jake Matthews</td>
      <td>OT</td>
      <td>11</td>
      <td>184</td>
      <td>184</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>Brian Habib</td>
      <td>G-T</td>
      <td>11</td>
      <td>183</td>
      <td>141</td>
      <td>0.770492</td>
    </tr>
    <tr>
      <td>Barry Sims</td>
      <td>T-G</td>
      <td>12</td>
      <td>181</td>
      <td>148</td>
      <td>0.817680</td>
    </tr>
    <tr>
      <td>Kelvin Beachum</td>
      <td>T</td>
      <td>13</td>
      <td>181</td>
      <td>163</td>
      <td>0.900552</td>
    </tr>
    <tr>
      <td>Chris Chester</td>
      <td>G</td>
      <td>11</td>
      <td>181</td>
      <td>153</td>
      <td>0.845304</td>
    </tr>
    <tr>
      <td>Mike Wilson</td>
      <td>T</td>
      <td>12</td>
      <td>180</td>
      <td>178</td>
      <td>0.988889</td>
    </tr>
    <tr>
      <td>Tyron Smith</td>
      <td>OT</td>
      <td>14</td>
      <td>180</td>
      <td>180</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>Orlando Pace</td>
      <td>T</td>
      <td>13</td>
      <td>179</td>
      <td>175</td>
      <td>0.977654</td>
    </tr>
    <tr>
      <td>John Parrella</td>
      <td>DT</td>
      <td>12</td>
      <td>179</td>
      <td>115</td>
      <td>0.642458</td>
    </tr>
    <tr>
      <td>Chad Clifton</td>
      <td>T</td>
      <td>12</td>
      <td>178</td>
      <td>173</td>
      <td>0.971910</td>
    </tr>
    <tr>
      <td>Ed Newman</td>
      <td>G</td>
      <td>12</td>
      <td>177</td>
      <td>119</td>
      <td>0.672316</td>
    </tr>
    <tr>
      <td>Leonard Davis</td>
      <td>T-G</td>
      <td>12</td>
      <td>177</td>
      <td>158</td>
      <td>0.892655</td>
    </tr>
    <tr>
      <td>Kareem McKenzie</td>
      <td>T</td>
      <td>11</td>
      <td>176</td>
      <td>168</td>
      <td>0.954545</td>
    </tr>
    <tr>
      <td>Bruce Davis</td>
      <td>T-G</td>
      <td>11</td>
      <td>176</td>
      <td>127</td>
      <td>0.721591</td>
    </tr>
    <tr>
      <td>Jordan Gross</td>
      <td>T</td>
      <td>11</td>
      <td>176</td>
      <td>176</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>David Diehl</td>
      <td>G-T</td>
      <td>11</td>
      <td>175</td>
      <td>171</td>
      <td>0.977143</td>
    </tr>
    <tr>
      <td>Matt Light</td>
      <td>T</td>
      <td>11</td>
      <td>175</td>
      <td>173</td>
      <td>0.988571</td>
    </tr>
    <tr>
      <td>Jeff Criswell</td>
      <td>T-G</td>
      <td>12</td>
      <td>174</td>
      <td>148</td>
      <td>0.850575</td>
    </tr>
    <tr>
      <td>Bobbie Williams</td>
      <td>G</td>
      <td>12</td>
      <td>173</td>
      <td>140</td>
      <td>0.809249</td>
    </tr>
    <tr>
      <td>Ryan Diem</td>
      <td>T-G</td>
      <td>11</td>
      <td>173</td>
      <td>166</td>
      <td>0.959538</td>
    </tr>
    <tr>
      <td>Doug Van Horn</td>
      <td>G-T</td>
      <td>14</td>
      <td>172</td>
      <td>154</td>
      <td>0.895349</td>
    </tr>
    <tr>
      <td>Dave Rowe</td>
      <td>DT-NT</td>
      <td>12</td>
      <td>172</td>
      <td>149</td>
      <td>0.866279</td>
    </tr>
    <tr>
      <td>Morgan Moses</td>
      <td>OT</td>
      <td>11</td>
      <td>171</td>
      <td>163</td>
      <td>0.953216</td>
    </tr>
    <tr>
      <td>Zack Martin</td>
      <td>G</td>
      <td>11</td>
      <td>171</td>
      <td>171</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>Ramon Foster</td>
      <td>T</td>
      <td>11</td>
      <td>171</td>
      <td>156</td>
      <td>0.912281</td>
    </tr>
    <tr>
      <td>James Williams</td>
      <td>T-DE-DT</td>
      <td>12</td>
      <td>170</td>
      <td>146</td>
      <td>0.858824</td>
    </tr>
    <tr>
      <td>Gerard Warren</td>
      <td>DT</td>
      <td>11</td>
      <td>170</td>
      <td>141</td>
      <td>0.829412</td>
    </tr>
    <tr>
      <td>Shaq Mason</td>
      <td>G</td>
      <td>10</td>
      <td>169</td>
      <td>164</td>
      <td>0.970414</td>
    </tr>
    <tr>
      <td>Dan Hampton</td>
      <td>DE-DT</td>
      <td>12</td>
      <td>169</td>
      <td>162</td>
      <td>0.958580</td>
    </tr>
    <tr>
      <td>Eric Winston</td>
      <td>T</td>
      <td>12</td>
      <td>168</td>
      <td>130</td>
      <td>0.773810</td>
    </tr>
    <tr>
      <td>Todd Perry</td>
      <td>G</td>
      <td>11</td>
      <td>168</td>
      <td>147</td>
      <td>0.875000</td>
    </tr>
    <tr>
      <td>Zach Strief</td>
      <td>G</td>
      <td>12</td>
      <td>168</td>
      <td>98</td>
      <td>0.583333</td>
    </tr>
    <tr>
      <td>Joe Walter</td>
      <td>T-G</td>
      <td>13</td>
      <td>168</td>
      <td>138</td>
      <td>0.821429</td>
    </tr>
    <tr>
      <td>John Ayers</td>
      <td>G-T</td>
      <td>11</td>
      <td>167</td>
      <td>147</td>
      <td>0.880240</td>
    </tr>
    <tr>
      <td>Jason Ferguson</td>
      <td>DT-NT</td>
      <td>13</td>
      <td>167</td>
      <td>135</td>
      <td>0.808383</td>
    </tr>
    <tr>
      <td>D\'Brickashaw Ferguson</td>
      <td>T</td>
      <td>10</td>
      <td>167</td>
      <td>167</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>Ephraim Salaam</td>
      <td>T</td>
      <td>13</td>
      <td>167</td>
      <td>133</td>
      <td>0.796407</td>
    </tr>
    <tr>
      <td>Michael Brockers</td>
      <td>DT</td>
      <td>11</td>
      <td>166</td>
      <td>163</td>
      <td>0.981928</td>
    </tr>
    <tr>
      <td>Ken Jones</td>
      <td>T-DE</td>
      <td>12</td>
      <td>166</td>
      <td>144</td>
      <td>0.867470</td>
    </tr>
    <tr>
      <td>George Starke</td>
      <td>T</td>
      <td>12</td>
      <td>166</td>
      <td>156</td>
      <td>0.939759</td>
    </tr>
    <tr>
      <td>Marco Rivera</td>
      <td>G</td>
      <td>10</td>
      <td>166</td>
      <td>149</td>
      <td>0.897590</td>
    </tr>
    <tr>
      <td>Greg Koch</td>
      <td>T-G</td>
      <td>11</td>
      <td>164</td>
      <td>148</td>
      <td>0.902439</td>
    </tr>
    <tr>
      <td>Joel Bitonio</td>
      <td>G</td>
      <td>11</td>
      <td>163</td>
      <td>163</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>Ken Ruettgers</td>
      <td>T</td>
      <td>12</td>
      <td>163</td>
      <td>147</td>
      <td>0.901840</td>
    </tr>
    <tr>
      <td>DaQuan Jones</td>
      <td>DT</td>
      <td>11</td>
      <td>163</td>
      <td>157</td>
      <td>0.963190</td>
    </tr>
    <tr>
      <td>Nate Solder</td>
      <td>T</td>
      <td>11</td>
      <td>162</td>
      <td>159</td>
      <td>0.981481</td>
    </tr>
    <tr>
      <td>Rich Baldinger</td>
      <td>G-T</td>
      <td>12</td>
      <td>162</td>
      <td>110</td>
      <td>0.679012</td>
    </tr>
    <tr>
      <td>Benji Olson</td>
      <td>G</td>
      <td>10</td>
      <td>161</td>
      <td>149</td>
      <td>0.925466</td>
    </tr>
    <tr>
      <td>Josh Sitton</td>
      <td>G</td>
      <td>11</td>
      <td>161</td>
      <td>151</td>
      <td>0.937888</td>
    </tr>
    <tr>
      <td>Ben Davidson</td>
      <td>DE-DT</td>
      <td>11</td>
      <td>161</td>
      <td>118</td>
      <td>0.732919</td>
    </tr>
    <tr>
      <td>Erik Williams</td>
      <td>T</td>
      <td>11</td>
      <td>161</td>
      <td>146</td>
      <td>0.906832</td>
    </tr>
    <tr>
      <td>Reggie Doss</td>
      <td>DE-DT</td>
      <td>10</td>
      <td>161</td>
      <td>95</td>
      <td>0.590062</td>
    </tr>
    <tr>
      <td>Tootie Robbins</td>
      <td>T</td>
      <td>12</td>
      <td>160</td>
      <td>148</td>
      <td>0.925000</td>
    </tr>
    <tr>
      <td>Stan Walters</td>
      <td>T</td>
      <td>12</td>
      <td>160</td>
      <td>155</td>
      <td>0.968750</td>
    </tr>
    <tr>
      <td>Herbert Scott</td>
      <td>G-T</td>
      <td>10</td>
      <td>160</td>
      <td>130</td>
      <td>0.812500</td>
    </tr>
    <tr>
      <td>Jason Fabini</td>
      <td>T</td>
      <td>11</td>
      <td>160</td>
      <td>137</td>
      <td>0.856250</td>
    </tr>
    <tr>
      <td>Joe Klecko</td>
      <td>DT-NT-DE</td>
      <td>12</td>
      <td>160</td>
      <td>147</td>
      <td>0.918750</td>
    </tr>
    <tr>
      <td>Doug Betters</td>
      <td>DE</td>
      <td>10</td>
      <td>159</td>
      <td>116</td>
      <td>0.729560</td>
    </tr>
    <tr>
      <td>Craig Wolfley</td>
      <td>G-T</td>
      <td>12</td>
      <td>159</td>
      <td>108</td>
      <td>0.679245</td>
    </tr>
    <tr>
      <td>Bruce Wilkerson</td>
      <td>T-G</td>
      <td>11</td>
      <td>158</td>
      <td>100</td>
      <td>0.632911</td>
    </tr>
    <tr>
      <td>Zefross Moss</td>
      <td>T</td>
      <td>11</td>
      <td>158</td>
      <td>141</td>
      <td>0.892405</td>
    </tr>
    <tr>
      <td>Alan Branch</td>
      <td>DT</td>
      <td>11</td>
      <td>158</td>
      <td>94</td>
      <td>0.594937</td>
    </tr>
    <tr>
      <td>Denico Autry</td>
      <td>DE</td>
      <td>11</td>
      <td>158</td>
      <td>95</td>
      <td>0.601266</td>
    </tr>
    <tr>
      <td>Matt Lepsis</td>
      <td>T</td>
      <td>10</td>
      <td>158</td>
      <td>138</td>
      <td>0.873418</td>
    </tr>
    <tr>
      <td>Harris Barton</td>
      <td>T-G</td>
      <td>10</td>
      <td>157</td>
      <td>153</td>
      <td>0.974522</td>
    </tr>
    <tr>
      <td>Grady Jarrett</td>
      <td>DT</td>
      <td>10</td>
      <td>157</td>
      <td>142</td>
      <td>0.904459</td>
    </tr>
    <tr>
      <td>Broderick Thompson</td>
      <td>T-G</td>
      <td>12</td>
      <td>156</td>
      <td>138</td>
      <td>0.884615</td>
    </tr>
    <tr>
      <td>Cody Risien</td>
      <td>T-G</td>
      <td>11</td>
      <td>156</td>
      <td>150</td>
      <td>0.961538</td>
    </tr>
    <tr>
      <td>James Hurst</td>
      <td>OT</td>
      <td>10</td>
      <td>156</td>
      <td>98</td>
      <td>0.628205</td>
    </tr>
    <tr>
      <td>Chris Canty</td>
      <td>DE</td>
      <td>11</td>
      <td>156</td>
      <td>135</td>
      <td>0.865385</td>
    </tr>
    <tr>
      <td>Jim Dombrowski</td>
      <td>G-T</td>
      <td>11</td>
      <td>155</td>
      <td>141</td>
      <td>0.909677</td>
    </tr>
    <tr>
      <td>T.J. Lang</td>
      <td>G-T</td>
      <td>10</td>
      <td>154</td>
      <td>124</td>
      <td>0.805195</td>
    </tr>
    <tr>
      <td>Jermon Bushrod</td>
      <td>T</td>
      <td>12</td>
      <td>154</td>
      <td>135</td>
      <td>0.876623</td>
    </tr>
    <tr>
      <td>Rob Havenstein</td>
      <td>OT</td>
      <td>10</td>
      <td>153</td>
      <td>153</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>Brandon Moore</td>
      <td>G</td>
      <td>10</td>
      <td>153</td>
      <td>151</td>
      <td>0.986928</td>
    </tr>
    <tr>
      <td>Chris Snee</td>
      <td>G</td>
      <td>10</td>
      <td>152</td>
      <td>152</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>Joe Carollo</td>
      <td>T</td>
      <td>12</td>
      <td>152</td>
      <td>119</td>
      <td>0.782895</td>
    </tr>
    <tr>
      <td>Elmer Collett</td>
      <td>G</td>
      <td>11</td>
      <td>152</td>
      <td>103</td>
      <td>0.677632</td>
    </tr>
    <tr>
      <td>Rudy Comstock</td>
      <td>G-T</td>
      <td>11</td>
      <td>152</td>
      <td>127</td>
      <td>0.835526</td>
    </tr>
    <tr>
      <td>Robert Brown</td>
      <td>DT-DE</td>
      <td>11</td>
      <td>152</td>
      <td>110</td>
      <td>0.723684</td>
    </tr>
    <tr>
      <td>Irv Eatman</td>
      <td>T</td>
      <td>11</td>
      <td>152</td>
      <td>120</td>
      <td>0.789474</td>
    </tr>
    <tr>
      <td>Billy Shields</td>
      <td>T</td>
      <td>11</td>
      <td>151</td>
      <td>126</td>
      <td>0.834437</td>
    </tr>
    <tr>
      <td>Doug Riesenberg</td>
      <td>T</td>
      <td>10</td>
      <td>151</td>
      <td>138</td>
      <td>0.913907</td>
    </tr>
    <tr>
      <td>Charles Leno Jr.</td>
      <td>OG</td>
      <td>10</td>
      <td>151</td>
      <td>143</td>
      <td>0.947020</td>
    </tr>
    <tr>
      <td>Dan Sullivan</td>
      <td>G-T</td>
      <td>11</td>
      <td>150</td>
      <td>98</td>
      <td>0.653333</td>
    </tr>
    <tr>
      <td>Charles Johnson</td>
      <td>DE</td>
      <td>11</td>
      <td>150</td>
      <td>120</td>
      <td>0.800000</td>
    </tr>
    <tr>
      <td>Ray Schoenke</td>
      <td>G-T</td>
      <td>13</td>
      <td>150</td>
      <td>102</td>
      <td>0.680000</td>
    </tr>
    <tr>
      <td>Roman Oben</td>
      <td>T</td>
      <td>12</td>
      <td>149</td>
      <td>135</td>
      <td>0.906040</td>
    </tr>
    <tr>
      <td>Harry Schuh</td>
      <td>T</td>
      <td>10</td>
      <td>149</td>
      <td>120</td>
      <td>0.805369</td>
    </tr>
    <tr>
      <td>Mike Tilleman</td>
      <td>DT</td>
      <td>11</td>
      <td>149</td>
      <td>137</td>
      <td>0.919463</td>
    </tr>
    <tr>
      <td>L.J. Shelton</td>
      <td>T</td>
      <td>10</td>
      <td>148</td>
      <td>127</td>
      <td>0.858108</td>
    </tr>
    <tr>
      <td>Tom Condon</td>
      <td>G</td>
      <td>12</td>
      <td>148</td>
      <td>131</td>
      <td>0.885135</td>
    </tr>
    <tr>
      <td>Wade Smith</td>
      <td>T</td>
      <td>12</td>
      <td>148</td>
      <td>102</td>
      <td>0.689189</td>
    </tr>
    <tr>
      <td>Ed Simmons</td>
      <td>T-G</td>
      <td>11</td>
      <td>147</td>
      <td>106</td>
      <td>0.721088</td>
    </tr>
    <tr>
      <td>Steve Riley</td>
      <td>T</td>
      <td>11</td>
      <td>147</td>
      <td>137</td>
      <td>0.931973</td>
    </tr>
    <tr>
      <td>Terron Armstead</td>
      <td>OT</td>
      <td>12</td>
      <td>146</td>
      <td>142</td>
      <td>0.972603</td>
    </tr>
    <tr>
      <td>Adam Snyder</td>
      <td>T-G</td>
      <td>10</td>
      <td>146</td>
      <td>90</td>
      <td>0.616438</td>
    </tr>
    <tr>
      <td>Randy Thomas</td>
      <td>G</td>
      <td>11</td>
      <td>146</td>
      <td>146</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>Evander Hood</td>
      <td>DT</td>
      <td>10</td>
      <td>146</td>
      <td>76</td>
      <td>0.520548</td>
    </tr>
    <tr>
      <td>Arik Armstead</td>
      <td>DE</td>
      <td>10</td>
      <td>145</td>
      <td>110</td>
      <td>0.758621</td>
    </tr>
    <tr>
      <td>Russell Okung</td>
      <td>T</td>
      <td>11</td>
      <td>145</td>
      <td>145</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>Mark Gastineau</td>
      <td>DE</td>
      <td>10</td>
      <td>144</td>
      <td>112</td>
      <td>0.777778</td>
    </tr>
    <tr>
      <td>Rufus Mayes</td>
      <td>T-G</td>
      <td>11</td>
      <td>144</td>
      <td>114</td>
      <td>0.791667</td>
    </tr>
    <tr>
      <td>Chris Samuels</td>
      <td>T</td>
      <td>10</td>
      <td>144</td>
      <td>144</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>Brandon Scherff</td>
      <td>G</td>
      <td>10</td>
      <td>144</td>
      <td>144</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>Ed Husmann</td>
      <td>DT-G-DE-LB</td>
      <td>13</td>
      <td>144</td>
      <td>104</td>
      <td>0.722222</td>
    </tr>
    <tr>
      <td>Derrick Dockery</td>
      <td>G</td>
      <td>10</td>
      <td>143</td>
      <td>117</td>
      <td>0.818182</td>
    </tr>
    <tr>
      <td>Marcus Cannon</td>
      <td>T</td>
      <td>12</td>
      <td>143</td>
      <td>88</td>
      <td>0.615385</td>
    </tr>
    <tr>
      <td>Bob Newton</td>
      <td>G-T</td>
      <td>11</td>
      <td>142</td>
      <td>108</td>
      <td>0.760563</td>
    </tr>
    <tr>
      <td>Kenyon Coleman</td>
      <td>DE</td>
      <td>11</td>
      <td>142</td>
      <td>81</td>
      <td>0.570423</td>
    </tr>
    <tr>
      <td>Bob Kowalkowski</td>
      <td>G</td>
      <td>12</td>
      <td>142</td>
      <td>102</td>
      <td>0.718310</td>
    </tr>
    <tr>
      <td>Ma\'ake Kemoeatu</td>
      <td>DT</td>
      <td>11</td>
      <td>142</td>
      <td>91</td>
      <td>0.640845</td>
    </tr>
    <tr>
      <td>Jon Jansen</td>
      <td>T</td>
      <td>11</td>
      <td>141</td>
      <td>129</td>
      <td>0.914894</td>
    </tr>
    <tr>
      <td>Ron Edwards</td>
      <td>DT</td>
      <td>12</td>
      <td>141</td>
      <td>98</td>
      <td>0.695035</td>
    </tr>
    <tr>
      <td>Gilbert Brown</td>
      <td>DT</td>
      <td>11</td>
      <td>141</td>
      <td>116</td>
      <td>0.822695</td>
    </tr>
    <tr>
      <td>Chris Clark</td>
      <td>T</td>
      <td>10</td>
      <td>141</td>
      <td>82</td>
      <td>0.581560</td>
    </tr>
    <tr>
      <td>Bill Owen</td>
      <td>T-G</td>
      <td>11</td>
      <td>140</td>
      <td>100</td>
      <td>0.714286</td>
    </tr>
    <tr>
      <td>Art Donovan</td>
      <td>DT-T</td>
      <td>12</td>
      <td>140</td>
      <td>138</td>
      <td>0.985714</td>
    </tr>
    <tr>
      <td>David Bakhtiari</td>
      <td>OT</td>
      <td>11</td>
      <td>140</td>
      <td>140</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>Len St. Jean</td>
      <td>G</td>
      <td>10</td>
      <td>140</td>
      <td>112</td>
      <td>0.800000</td>
    </tr>
    <tr>
      <td>Paul Soliai</td>
      <td>DT</td>
      <td>10</td>
      <td>139</td>
      <td>87</td>
      <td>0.625899</td>
    </tr>
    <tr>
      <td>Bryan Bulaga</td>
      <td>T</td>
      <td>12</td>
      <td>139</td>
      <td>135</td>
      <td>0.971223</td>
    </tr>
    <tr>
      <td>Bruce Reimers</td>
      <td>G-T</td>
      <td>10</td>
      <td>139</td>
      <td>95</td>
      <td>0.683453</td>
    </tr>
    <tr>
      <td>Evan Mathis</td>
      <td>G</td>
      <td>12</td>
      <td>139</td>
      <td>98</td>
      <td>0.705036</td>
    </tr>
    <tr>
      <td>Edwin Mulitalo</td>
      <td>G</td>
      <td>10</td>
      <td>139</td>
      <td>135</td>
      <td>0.971223</td>
    </tr>
    <tr>
      <td>John Wooten</td>
      <td>G</td>
      <td>10</td>
      <td>139</td>
      <td>110</td>
      <td>0.791367</td>
    </tr>
    <tr>
      <td>Jim Lachey</td>
      <td>T</td>
      <td>11</td>
      <td>138</td>
      <td>136</td>
      <td>0.985507</td>
    </tr>
    <tr>
      <td>Marvin Powell</td>
      <td>T</td>
      <td>11</td>
      <td>138</td>
      <td>135</td>
      <td>0.978261</td>
    </tr>
    <tr>
      <td>John Brown</td>
      <td>T</td>
      <td>10</td>
      <td>138</td>
      <td>101</td>
      <td>0.731884</td>
    </tr>
    <tr>
      <td>Jon Giesler</td>
      <td>T</td>
      <td>10</td>
      <td>138</td>
      <td>116</td>
      <td>0.840580</td>
    </tr>
    <tr>
      <td>Demar Dotson</td>
      <td>T</td>
      <td>12</td>
      <td>138</td>
      <td>114</td>
      <td>0.826087</td>
    </tr>
    <tr>
      <td>Kendall Langford</td>
      <td>DE</td>
      <td>10</td>
      <td>137</td>
      <td>114</td>
      <td>0.832117</td>
    </tr>
    <tr>
      <td>James Carpenter</td>
      <td>LG</td>
      <td>11</td>
      <td>137</td>
      <td>127</td>
      <td>0.927007</td>
    </tr>
    <tr>
      <td>Steve Wright</td>
      <td>T-G-TE</td>
      <td>12</td>
      <td>137</td>
      <td>70</td>
      <td>0.510949</td>
    </tr>
    <tr>
      <td>Sam Adams</td>
      <td>G-T</td>
      <td>10</td>
      <td>137</td>
      <td>123</td>
      <td>0.897810</td>
    </tr>
    <tr>
      <td>George Musso</td>
      <td>G-T</td>
      <td>12</td>
      <td>136</td>
      <td>89</td>
      <td>0.654412</td>
    </tr>
    <tr>
      <td>John Gordy</td>
      <td>G-T</td>
      <td>11</td>
      <td>136</td>
      <td>128</td>
      <td>0.941176</td>
    </tr>
    <tr>
      <td>Corbin Lacina</td>
      <td>G</td>
      <td>10</td>
      <td>135</td>
      <td>82</td>
      <td>0.607407</td>
    </tr>
    <tr>
      <td>Earl Dotson</td>
      <td>T</td>
      <td>10</td>
      <td>135</td>
      <td>99</td>
      <td>0.733333</td>
    </tr>
    <tr>
      <td>Jermane Mayberry</td>
      <td>G-T</td>
      <td>10</td>
      <td>134</td>
      <td>114</td>
      <td>0.850746</td>
    </tr>
    <tr>
      <td>Conrad Dobler</td>
      <td>G</td>
      <td>10</td>
      <td>134</td>
      <td>129</td>
      <td>0.962687</td>
    </tr>
    <tr>
      <td>Justin Pugh</td>
      <td>OG</td>
      <td>11</td>
      <td>134</td>
      <td>133</td>
      <td>0.992537</td>
    </tr>
    <tr>
      <td>Mickey Marvin</td>
      <td>G</td>
      <td>11</td>
      <td>133</td>
      <td>119</td>
      <td>0.894737</td>
    </tr>
    <tr>
      <td>Joe Bostic</td>
      <td>G-T</td>
      <td>10</td>
      <td>133</td>
      <td>116</td>
      <td>0.872180</td>
    </tr>
    <tr>
      <td>John Jerry</td>
      <td>G</td>
      <td>10</td>
      <td>133</td>
      <td>107</td>
      <td>0.804511</td>
    </tr>
    <tr>
      <td>Orlando Brown</td>
      <td>T</td>
      <td>12</td>
      <td>132</td>
      <td>122</td>
      <td>0.924242</td>
    </tr>
    <tr>
      <td>Andrus Peat</td>
      <td>OT</td>
      <td>10</td>
      <td>132</td>
      <td>109</td>
      <td>0.825758</td>
    </tr>
    <tr>
      <td>Kevin Call</td>
      <td>T</td>
      <td>10</td>
      <td>131</td>
      <td>88</td>
      <td>0.671756</td>
    </tr>
    <tr>
      <td>Dave Herman</td>
      <td>G-T</td>
      <td>10</td>
      <td>131</td>
      <td>121</td>
      <td>0.923664</td>
    </tr>
    <tr>
      <td>Bruce Van Dyke</td>
      <td>G</td>
      <td>11</td>
      <td>131</td>
      <td>124</td>
      <td>0.946565</td>
    </tr>
    <tr>
      <td>Chris Liwienski</td>
      <td>G-T</td>
      <td>10</td>
      <td>130</td>
      <td>96</td>
      <td>0.738462</td>
    </tr>
    <tr>
      <td>Dave Reavis</td>
      <td>T-G</td>
      <td>10</td>
      <td>130</td>
      <td>89</td>
      <td>0.684615</td>
    </tr>
    <tr>
      <td>Vince Promuto</td>
      <td>G</td>
      <td>11</td>
      <td>130</td>
      <td>113</td>
      <td>0.869231</td>
    </tr>
    <tr>
      <td>Jim Cadile</td>
      <td>G-T</td>
      <td>11</td>
      <td>129</td>
      <td>107</td>
      <td>0.829457</td>
    </tr>
    <tr>
      <td>Jeff Blackshear</td>
      <td>G</td>
      <td>10</td>
      <td>129</td>
      <td>96</td>
      <td>0.744186</td>
    </tr>
    <tr>
      <td>Anthony Clement</td>
      <td>T</td>
      <td>10</td>
      <td>129</td>
      <td>108</td>
      <td>0.837209</td>
    </tr>
    <tr>
      <td>Bob Brown</td>
      <td>T</td>
      <td>10</td>
      <td>128</td>
      <td>126</td>
      <td>0.984375</td>
    </tr>
    <tr>
      <td>Harvey Salem</td>
      <td>T-G</td>
      <td>10</td>
      <td>128</td>
      <td>107</td>
      <td>0.835938</td>
    </tr>
    <tr>
      <td>Fuzzy Thurston</td>
      <td>G</td>
      <td>10</td>
      <td>127</td>
      <td>97</td>
      <td>0.763780</td>
    </tr>
    <tr>
      <td>Vaughn Parker</td>
      <td>T</td>
      <td>11</td>
      <td>126</td>
      <td>108</td>
      <td>0.857143</td>
    </tr>
    <tr>
      <td>Andre Smith</td>
      <td>T</td>
      <td>13</td>
      <td>126</td>
      <td>102</td>
      <td>0.809524</td>
    </tr>
    <tr>
      <td>Walt Kiesling</td>
      <td>G-T</td>
      <td>13</td>
      <td>126</td>
      <td>81</td>
      <td>0.642857</td>
    </tr>
    <tr>
      <td>Terry Hermeling</td>
      <td>T-G-DE</td>
      <td>11</td>
      <td>125</td>
      <td>108</td>
      <td>0.864000</td>
    </tr>
    <tr>
      <td>Matt Herkenhoff</td>
      <td>T</td>
      <td>10</td>
      <td>125</td>
      <td>122</td>
      <td>0.976000</td>
    </tr>
    <tr>
      <td>Damion McIntosh</td>
      <td>T</td>
      <td>10</td>
      <td>125</td>
      <td>113</td>
      <td>0.904000</td>
    </tr>
    <tr>
      <td>Matt O\'Dwyer</td>
      <td>G</td>
      <td>10</td>
      <td>124</td>
      <td>107</td>
      <td>0.862903</td>
    </tr>
    <tr>
      <td>Seth Payne</td>
      <td>DT-NT</td>
      <td>10</td>
      <td>124</td>
      <td>99</td>
      <td>0.798387</td>
    </tr>
    <tr>
      <td>Matt Joyce</td>
      <td>G-T</td>
      <td>10</td>
      <td>124</td>
      <td>71</td>
      <td>0.572581</td>
    </tr>
    <tr>
      <td>Wade Key</td>
      <td>G-T</td>
      <td>10</td>
      <td>124</td>
      <td>118</td>
      <td>0.951613</td>
    </tr>
    <tr>
      <td>Bob Heinz</td>
      <td>DT-DE</td>
      <td>10</td>
      <td>122</td>
      <td>65</td>
      <td>0.532787</td>
    </tr>
    <tr>
      <td>Brandon Brooks</td>
      <td>G</td>
      <td>10</td>
      <td>122</td>
      <td>114</td>
      <td>0.934426</td>
    </tr>
    <tr>
      <td>Ray Krouse</td>
      <td>DT-DE-T</td>
      <td>10</td>
      <td>122</td>
      <td>91</td>
      <td>0.745902</td>
    </tr>
    <tr>
      <td>Bubba Smith</td>
      <td>DE-DT</td>
      <td>10</td>
      <td>122</td>
      <td>93</td>
      <td>0.762295</td>
    </tr>
    <tr>
      <td>Travelle Wharton</td>
      <td>T-G</td>
      <td>10</td>
      <td>120</td>
      <td>116</td>
      <td>0.966667</td>
    </tr>
    <tr>
      <td>Garry Puetz</td>
      <td>G-T</td>
      <td>10</td>
      <td>120</td>
      <td>73</td>
      <td>0.608333</td>
    </tr>
    <tr>
      <td>Richard Neal</td>
      <td>DE-DT</td>
      <td>10</td>
      <td>120</td>
      <td>96</td>
      <td>0.800000</td>
    </tr>
    <tr>
      <td>Ryan Harris</td>
      <td>T</td>
      <td>10</td>
      <td>119</td>
      <td>73</td>
      <td>0.613445</td>
    </tr>
    <tr>
      <td>Reggie Wells</td>
      <td>G-T</td>
      <td>10</td>
      <td>119</td>
      <td>93</td>
      <td>0.781513</td>
    </tr>
    <tr>
      <td>Brett Miller</td>
      <td>T</td>
      <td>10</td>
      <td>118</td>
      <td>63</td>
      <td>0.533898</td>
    </tr>
    <tr>
      <td>Erik Pears</td>
      <td>T</td>
      <td>10</td>
      <td>117</td>
      <td>102</td>
      <td>0.871795</td>
    </tr>
    <tr>
      <td>Marc Colombo</td>
      <td>T</td>
      <td>10</td>
      <td>115</td>
      <td>99</td>
      <td>0.860870</td>
    </tr>
    <tr>
      <td>Alex Boone</td>
      <td>T</td>
      <td>11</td>
      <td>114</td>
      <td>92</td>
      <td>0.807018</td>
    </tr>
    <tr>
      <td>Doug Dawson</td>
      <td>G</td>
      <td>11</td>
      <td>113</td>
      <td>77</td>
      <td>0.681416</td>
    </tr>
    <tr>
      <td>Ed Cook</td>
      <td>T-G</td>
      <td>10</td>
      <td>112</td>
      <td>68</td>
      <td>0.607143</td>
    </tr>
    <tr>
      <td>Kris Jenkins</td>
      <td>DT</td>
      <td>10</td>
      <td>112</td>
      <td>106</td>
      <td>0.946429</td>
    </tr>
    <tr>
      <td>Will Montgomery</td>
      <td>G</td>
      <td>10</td>
      <td>112</td>
      <td>77</td>
      <td>0.687500</td>
    </tr>
    <tr>
      <td>Clarence Jones</td>
      <td>T</td>
      <td>10</td>
      <td>111</td>
      <td>88</td>
      <td>0.792793</td>
    </tr>
    <tr>
      <td>Billy Turner</td>
      <td>OT</td>
      <td>10</td>
      <td>110</td>
      <td>82</td>
      <td>0.745455</td>
    </tr>
    <tr>
      <td>Derrick Burgess</td>
      <td>DE-LB</td>
      <td>10</td>
      <td>109</td>
      <td>76</td>
      <td>0.697248</td>
    </tr>
    <tr>
      <td>Adam Meadows</td>
      <td>T</td>
      <td>10</td>
      <td>109</td>
      <td>102</td>
      <td>0.935780</td>
    </tr>
    <tr>
      <td>Chris Hubbard</td>
      <td>G</td>
      <td>11</td>
      <td>108</td>
      <td>61</td>
      <td>0.564815</td>
    </tr>
    <tr>
      <td>Keydrick Vincent</td>
      <td>G</td>
      <td>10</td>
      <td>108</td>
      <td>87</td>
      <td>0.805556</td>
    </tr>
    <tr>
      <td>Trent Brown</td>
      <td>OT</td>
      <td>10</td>
      <td>107</td>
      <td>100</td>
      <td>0.934579</td>
    </tr>
    <tr>
      <td>Tony Pashos</td>
      <td>T</td>
      <td>10</td>
      <td>107</td>
      <td>85</td>
      <td>0.794393</td>
    </tr>
    <tr>
      <td>Daniel Kilgore</td>
      <td>G</td>
      <td>10</td>
      <td>106</td>
      <td>60</td>
      <td>0.566038</td>
    </tr>
    <tr>
      <td>Bob Kilcullen</td>
      <td>DT-DE-T</td>
      <td>10</td>
      <td>105</td>
      <td>57</td>
      <td>0.542857</td>
    </tr>
    <tr>
      <td>Willie Colon</td>
      <td>G</td>
      <td>10</td>
      <td>104</td>
      <td>104</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <td>Frank Cope</td>
      <td>T</td>
      <td>10</td>
      <td>104</td>
      <td>64</td>
      <td>0.615385</td>
    </tr>
    <tr>
      <td>Gordon King</td>
      <td>T-G</td>
      <td>10</td>
      <td>102</td>
      <td>64</td>
      <td>0.627451</td>
    </tr>
    <tr>
      <td>Josh Evans</td>
      <td>DT</td>
      <td>10</td>
      <td>100</td>
      <td>59</td>
      <td>0.590000</td>
    </tr>
    <tr>
      <td>Jim Skaggs</td>
      <td>G-T</td>
      <td>10</td>
      <td>100</td>
      <td>83</td>
      <td>0.830000</td>
    </tr>
    <tr>
      <td>Ken Sanders</td>
      <td>DE</td>
      <td>10</td>
      <td>100</td>
      <td>78</td>
      <td>0.780000</td>
    </tr>
    <tr>
      <td>Breno Giacomini</td>
      <td>G</td>
      <td>10</td>
      <td>99</td>
      <td>91</td>
      <td>0.919192</td>
    </tr>
    <tr>
      <td>Eddie Goldman</td>
      <td>DT</td>
      <td>10</td>
      <td>99</td>
      <td>84</td>
      <td>0.848485</td>
    </tr>
    <tr>
      <td>Steve Owen</td>
      <td>T-G</td>
      <td>10</td>
      <td>98</td>
      <td>84</td>
      <td>0.857143</td>
    </tr>
    <tr>
      <td>J\'Marcus Webb</td>
      <td>T</td>
      <td>11</td>
      <td>98</td>
      <td>75</td>
      <td>0.765306</td>
    </tr>
    <tr>
      <td>Stan Campbell</td>
      <td>G</td>
      <td>11</td>
      <td>97</td>
      <td>68</td>
      <td>0.701031</td>
    </tr>
    <tr>
      <td>Conway Baker</td>
      <td>G-T</td>
      <td>10</td>
      <td>96</td>
      <td>54</td>
      <td>0.562500</td>
    </tr>
    <tr>
      <td>Dick Stahlman</td>
      <td>T-G</td>
      <td>10</td>
      <td>70</td>
      <td>50</td>
      <td>0.714286</td>
    </tr>
    <tr>
      <td>Eddie Michaels</td>
      <td>G</td>
      <td>11</td>
      <td>63</td>
      <td>38</td>
      <td>0.603175</td>
    </tr>
    <tr>
      <td>Al Jolley</td>
      <td>T</td>
      <td>10</td>
      <td>35</td>
      <td>26</td>
      <td>0.742857</td>
    </tr>
  </tbody>
</table>

</details>

There are 267 players on the full list. Mostly offensive linemen, with some defensive linemen in there too. Without extensive statistics to look at, I'm turning to accolades. Even still, there are so many Pro Bowls, All-Pro teams, and Super Bowls rings across this list that it becomes incredibly tricky to compare them to each other. Luckily for me, I don't personally need to compare these players' careers, as the broader football community has already done this, and chose to give the highest honor to 10 of them. All of the following players have been inducted into the Pro Football Hall of Fame. [^2]

- [Larry Allen (G-T)](https://www.pro-football-reference.com/players/A/AlleLa00.htm)
- [Winston Hill (T)](https://www.pro-football-reference.com/players/H/HillWi00.htm)
- [Larry Little (G-T)](https://www.pro-football-reference.com/players/L/LittLa00.htm)
- [Willie Roaf (T)](https://www.pro-football-reference.com/players/R/RoafWi00.htm)
- [Walter Jones (T)](https://www.pro-football-reference.com/players/J/JoneWa00.htm)
- [Joe DeLamielleure (G)](https://www.pro-football-reference.com/players/D/DeLaJo01.htm)
- [Orlando Pace (T)](https://www.pro-football-reference.com/players/P/PaceOr00.htm)
- [Dan Hampton (DE-DT)](https://www.pro-football-reference.com/players/H/HampDa01.htm)
- [Joe Klecko (DT-NT-DE)](https://www.pro-football-reference.com/players/K/KlecJo00.htm)
- [Art Donovan (DT-T)](https://www.pro-football-reference.com/players/D/DonoAr00.htm)

From here, selecting the best player gets hazy. Staying true to the original question, Walter Jones has the fewest fumble recoveries on this entire list. So he may be the best answer if you value minimizing total posessions. Dan Hampton and Joe Klecko are the only two defensive players from the modern era of the NFL. Hampton edges out Klecko in sacks, at 82.5 versus 78, but Klecko transistioned to a nose tackle at the end of his career, trading sacks numbers for impactful run stopping.

## My Pick
Personally, my pick for the best player is Larry Allen. He has only 4 fumble recoveries in over 200 games played, the most on the list, with some of the most impressive accolades out there. A Super Bowl champion, he made 11 Pro Bowls, 6 All-Pro teams, and both the 1990s and 2000s Hall of Fame all decade teams. The most impressive part to me is his versatility on the offensive line. He started his career at right tackle, before being moved to right guard. As a guard, he was given 2 first team All-Pro honors and selected to 3 consecutive Pro Bowls, despite splitting time between guard and left tackle in the third season due to injuries. The next season, he started at left tackle, protecting Troy Aikman's blindside. In this year, he received yet another first team All-Pro nod and Pro Bowl selection, becoming the first player to do so at 2 different offensive lineman positions. On top of that, the Dallas offensive line gave up just 19 sacks on 493 pass plays, anchored by Larry Allen on the blindside. After that year, he moved to left guard, where he stayed for the rest of his career, and continued to dominate. While my approach is unscientific and contains quite a few personal judgements, I declare Larry Allen to be the best NFL player to never carry the football. 

If you took the time to read all this, thank you. Check back again soon to stay up to date on my recent blog posts.

[^1]: On top of these fumbles, it seems like Ruddy also has a postgame reception in 1998. Not sure why my scraper missed that one, as Ruddy's postseason targets, receptions, and receiving yards all show as 0 in my dataset. It's certainly something for me to look into, regardless of the fact that he's not our winner for this question.
[^2]: Looking only at Hall of Famers excludes any active players or recently retired players, but this seems alright to me. Maybe I'll revisit this topic in ten years to see how things have changed.