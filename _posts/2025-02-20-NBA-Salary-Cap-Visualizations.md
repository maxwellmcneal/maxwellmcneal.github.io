---
layout: post
author: Maxwell McNeal
title: NBA Salary Cap Visualizations
excerpt: Graphs about NBA teams' financial situations
---

I find the financial management side of the NBA almost just as interesting as the on-court product sometimes. The most recent CBA has introduced many new rules that greatly affect roster construction and the optimal way to build a team to maximize the length of a championship window. Out of curiosity, I decided to make some data visualizations of the current financial state of each NBA team as of the All-Star Break, or February 18th 2025. All of the following data comes from [Spotrac.com](https://www.spotrac.com/nba/cap/_/year/2024/sort/cap_maximum_space).

## Total Active Salary

{% include plots/2025-02-20/salary_by_team.html %}
<br>
The chart above shows the total salary cap hit of all the active players on each NBA team. This helps visualize the basic finanical situation of each NBA team. All the top teams in active salary are essentially in "win now" mode. They have big name veterans, like LeBron James, Kevin Durant, and Rudy Gobert who command large contracts. This has pushed their teams well over the luxury tax and over the first and second apron limits. The restrictions and hefty luxury tax payments that come with being over the apron limits, especially in consecutive years, will eventually force these teams to shed salary by cutting players or trading them for cheaper contracts, likely hurting their chances of seriously competing for a championship. The other end of the spectrum shows teams that are either starting or in the middle of a rebuild. Keeping the team's salary cost low helps the team avoid any restrictions or big luxury tax bills and allows them the financial flexibility to sign necessary free agents as they begin to compete in the league.

## Cost Per Win

{% include plots/2025-02-20/cost_per_win.html %}
<br>
While spending money may help a team be more competitive, it's possible to build a winning team in other ways. This chart shows each team's active salary divided by their number of wins, as of the All-Star break. From this chart, we see that the Thunder and the Cavs are spending the least amount of money per win. This makes sense, given that both teams are highly successful this season and have primarily built their team via the draft. Both teams have multiple key contributors on economical rookie deals, allowing them to win without crossing the luxury tax limit. On the other side of the spectrum, we have the Wizards. With the worst record in the league, they have taken on expensive veteran contracts of players like Marcus Smart and Khris Middleton at the trade deadline in exchange for draft capital to begin a rebuild.

## Individual Team Situations
Below are two charts for each team. The first chart shows each teams' total cap allocation, broken down by individual player. This helps visualize what players command the most money on each roster, as well as the current contract situation for each player. I found it interesting to visually see the value of role/bench players compared to the enormous max and supermax contracts in the league. The second is a donut chart showing the percentage of each team's total cap allocation spent on active players, dead money (cut/bought out players), and cap holds. All teams spend the majority of their total cap allocation on active players, but some teams have interesting dead money situations, such as the Nets' huge dead money percentage due to buying Ben Simmons out of his contract. Cap holds are generally less important, with some teams retaining meaningless cap holds on players that have retired years ago. 

Click the dropdown menu below for easy navigation to any individual team.
<br>
<details>
<summary> Full Team List </summary>
<ul>
        <li><a href='#atlanta-hawks'>Atlanta Hawks</a></li>
        <li><a href='#boston-celtics'>Boston Celtics</a></li>
        <li><a href='#brooklyn-nets'>Brooklyn Nets</a></li>
        <li><a href='#charlotte-hornets'>Charlotte Hornets</a></li>
        <li><a href='#chicago-bulls'>Chicago Bulls</a></li>
        <li><a href='#cleveland-cavaliers'>Cleveland Cavaliers</a></li>
        <li><a href='#dallas-mavericks'>Dallas Mavericks</a></li>
        <li><a href='#denver-nuggets'>Denver Nuggets</a></li>
        <li><a href='#detroit-pistons'>Detroit Pistons</a></li>
        <li><a href='#golden-state-warriors'>Golden State Warriors</a></li>
        <li><a href='#houston-rockets'>Houston Rockets</a></li>
        <li><a href='#indiana-pacers'>Indiana Pacers</a></li>
        <li><a href='#la-clippers'>LA Clippers</a></li>
        <li><a href='#los-angeles-lakers'>Los Angeles Lakers</a></li>
        <li><a href='#memphis-grizzlies'>Memphis Grizzlies</a></li>
        <li><a href='#miami-heat'>Miami Heat</a></li>
        <li><a href='#milwaukee-bucks'>Milwaukee Bucks</a></li>
        <li><a href='#minnesota-timberwolves'>Minnesota Timberwolves</a></li>
        <li><a href='#new-orleans-pelicans'>New Orleans Pelicans</a></li>
        <li><a href='#new-york-knicks'>New York Knicks</a></li>
        <li><a href='#oklahoma-city-thunder'>Oklahoma City Thunder</a></li>
        <li><a href='#orlando-magic'>Orlando Magic</a></li>
        <li><a href='#philadelphia-76ers'>Philadelphia 76ers</a></li>
        <li><a href='#phoenix-suns'>Phoenix Suns</a></li>
        <li><a href='#portland-trail-blazers'>Portland Trail Blazers</a></li>
        <li><a href='#sacramento-kings'>Sacramento Kings</a></li>
        <li><a href='#san-antonio-spurs'>San Antonio Spurs</a></li>
        <li><a href='#toronto-raptors'>Toronto Raptors</a></li>
        <li><a href='#utah-jazz'>Utah Jazz</a></li>
        <li><a href='#washington-wizards'>Washington Wizards</a></li>
</ul>
</details>

### Atlanta Hawks
{% include plots/2025-02-20/bar_plot_ATL.html %}
<br>
{% include plots/2025-02-20/donut_plot_ATL.html %}

### Boston Celtics
{% include plots/2025-02-20/bar_plot_BOS.html %}
<br>
{% include plots/2025-02-20/donut_plot_BOS.html %}

### Brooklyn Nets
{% include plots/2025-02-20/bar_plot_BKN.html %}
<br>
{% include plots/2025-02-20/donut_plot_BKN.html %}

### Charlotte Hornets
{% include plots/2025-02-20/bar_plot_CHA.html %}
<br>
{% include plots/2025-02-20/donut_plot_CHA.html %}

### Chicago Bulls
{% include plots/2025-02-20/bar_plot_CHI.html %}
<br>
{% include plots/2025-02-20/donut_plot_CHI.html %}

### Cleveland Cavaliers
{% include plots/2025-02-20/bar_plot_CLE.html %}
<br>
{% include plots/2025-02-20/donut_plot_CLE.html %}

### Dallas Mavericks
{% include plots/2025-02-20/bar_plot_DAL.html %}
<br>
{% include plots/2025-02-20/donut_plot_DAL.html %}

### Denver Nuggets
{% include plots/2025-02-20/bar_plot_DEN.html %}
<br>
{% include plots/2025-02-20/donut_plot_DEN.html %}

### Detroit Pistons
{% include plots/2025-02-20/bar_plot_DET.html %}
<br>
{% include plots/2025-02-20/donut_plot_DET.html %}

### Golden State Warriors
{% include plots/2025-02-20/bar_plot_GSW.html %}
<br>
{% include plots/2025-02-20/donut_plot_GSW.html %}

### Houston Rockets
{% include plots/2025-02-20/bar_plot_HOU.html %}
<br>
{% include plots/2025-02-20/donut_plot_HOU.html %}

### Indiana Pacers
{% include plots/2025-02-20/bar_plot_IND.html %}
<br>
{% include plots/2025-02-20/donut_plot_IND.html %}

### LA Clippers
{% include plots/2025-02-20/bar_plot_LAC.html %}
<br>
{% include plots/2025-02-20/donut_plot_LAC.html %}

### Los Angeles Lakers
{% include plots/2025-02-20/bar_plot_LAL.html %}
<br>
{% include plots/2025-02-20/donut_plot_LAL.html %}

### Memphis Grizzlies
{% include plots/2025-02-20/bar_plot_MEM.html %}
<br>
{% include plots/2025-02-20/donut_plot_MEM.html %}

### Miami Heat
{% include plots/2025-02-20/bar_plot_MIA.html %}
<br>
{% include plots/2025-02-20/donut_plot_MIA.html %}

### Milwaukee Bucks
{% include plots/2025-02-20/bar_plot_MIL.html %}
<br>
{% include plots/2025-02-20/donut_plot_MIL.html %}

### Minnesota Timberwolves
{% include plots/2025-02-20/bar_plot_MIN.html %}
<br>
{% include plots/2025-02-20/donut_plot_MIN.html %}

### New Orleans Pelicans
{% include plots/2025-02-20/bar_plot_NOP.html %}
<br>
{% include plots/2025-02-20/donut_plot_NOP.html %}

### New York Knicks
{% include plots/2025-02-20/bar_plot_NYK.html %}
<br>
{% include plots/2025-02-20/donut_plot_NYK.html %}

### Orlando Magic
{% include plots/2025-02-20/bar_plot_ORL.html %}
<br>
{% include plots/2025-02-20/donut_plot_ORL.html %}

### Portland Trail Blazers
{% include plots/2025-02-20/bar_plot_POR.html %}
<br>
{% include plots/2025-02-20/donut_plot_POR.html %}

### Sacramento Kings
{% include plots/2025-02-20/bar_plot_SAC.html %}
<br>
{% include plots/2025-02-20/donut_plot_SAC.html %}

### Toronto Raptors
{% include plots/2025-02-20/bar_plot_TOR.html %}
<br>
{% include plots/2025-02-20/donut_plot_TOR.html %}

### Utah Jazz
{% include plots/2025-02-20/bar_plot_UTA.html %}
<br>
{% include plots/2025-02-20/donut_plot_UTA.html %}

### Washington Wizards
{% include plots/2025-02-20/bar_plot_WAS.html %}
<br>
{% include plots/2025-02-20/donut_plot_WAS.html %}