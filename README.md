# Closure: A Statistical Look at my Dota 2 Career

<img src="Pictures\dota_2_official_9.jpg"></img>

## Introduction

[Jupyter Nbviewer Version](https://nbviewer.jupyter.org/github/billwarker/opendota-analysis/blob/master/A%20Statistical%20Look%20Back%20on%20my%20Dota%202%20Career.ipynb)

### A Brief History of DotA

Have you ever been addicted? Smoking? Sex? Gambling? Hard drugs? While other folks were out pursuing these exciting vices during their youth, I was staying inside playing DotA.

DotA (short for Defense of the Ancients) is a five-versus-five online multiplayer strategy videogame, with its origins going all the way back to Blizzard Entertainment's *Warcraft 3* released in 2003. Originally a custom gamemode created by a community member by the name of 'Icefrog' in Warcraft's *Frozen Throne* expansion, DotA grew to be one of [the most played and influential online strategy games of all time](https://www.youtube.com/watch?v=qTsaS1Tm-Ic). With players all over the world playing what was essentially a fan-made spinoff, a competitive scene emmerged and DotA became among the first wave of serious eSports titles. It pioneered the "Multiplayer Online Battle Arena" (MOBA) genre of strategy games, and was subsequently ripped off hard by games like *League of Legends* years afterwards (I had to say it).

I started playing the original DotA in middle school, after my best friend helped me download a cracked version of *Frozen Throne* onto my first laptop. DotA is not an easy game - I was bad, for a long time. I almost gave up many times, but like any great pursuit in life, perseverance eventually rewarded me with some moderate level of success. I didn't completely suck, and the thrill of beating up on players who did was exhiliharating.

In 2011, Valve Corporation hired on Icefrog to create Dota 2 - a full-fledged, fully-funded sequel to his famous community mod. A public beta for the game launched in 2012, and I was among the first initial waves of testers to see DotA brought to a new era. Since its official release in 2013, Dota 2 has grown to be one of the biggest eSports in the world. The day prior to me writing this introduction, a professional team of players (Team Liquid) walked away with $10 million dollars for winning *The International*, Valve's seventh annual international Dota 2 tournament.

Dota 2 is a wonderfully strategic and rewarding game enjoyed daily by hundreds of thousands of players around the world. Since stats started being tracked on player activity in 2012, I've played 3647 matches. That being said, anyone who's ever played Dota 2 can tell you how addicting and toxic it is, too. Between awful teammates, thrown matches and cheesy strategies, Dota 2 can hollow out your soul if you play it long enough. It's like the black-tar heroin of online videogames, and earlier this year I kicked it for good.

### Why I'm doing this Analysis

Since DotA is a team game, the statistics of my individual performance aren't completely reliable indicators on whether I would win a certain match or not. There are also many other variables, such as matchmaking rating, item builds, and gold graphs that are beyond the scope of the data I have available. Given what I do have, I believe it's entirely possible to highlight some relationships between the general elements of my own gameplay.

For most of this analysis I'm going to examine the relationship between match result and the other variables in the dataset, since winning is the ultimate goal in each game of DotA. To rephrase this as a research question: **which aspects of my gameplay make me more likely to win or lose a match?** My hope for this analysis is provide some statistical evidence for the intuitions I've built up over 3000+ games.

For readers who aren't familiar with DotA, [here's a short video that'll give you the gist of what the game is about](https://www.youtube.com/watch?v=Cp8neRiF9-k). To get the most out of this analysis I'm going to go into a moderate amount of detail about gameplay mechanics and general strategy, but I'll explain these things as I go along.

Personally, going the history of my Dota 2 career serves as the necessary closure to let go of the game for good. It's a love-hate kind of thing; the lows were so low, but the highs were so high. It'll be fun taking a trip down memory lane, even if all the memories weren't that great.

### The Data

All of my match data was sourced from [OpenDota](https://www.opendota.com/), an open-source data platform that grabs its data directly from Steam. OpenDota provides a great [API](https://docs.opendota.com/) for developers to build their own applications with. The data I'll be working with comes from two GET requests to the API; one for my match data, and one for general hero data. I loaded this data into a MySQL database and exported it into two CSV files - one with my match data joined with hero data, and the hero data on its own - which I'll work with using Python's Pandas module. The code and CSVs I used for all of this can be found [here](https://github.com/billwarker/opendota-analysis).
