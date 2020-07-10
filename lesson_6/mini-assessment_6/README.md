####  Australian Football League Team and Player's Performance Analysis-Season 2012-2018

The dataset for this analysis is downloaded from [kaggle](https://www.kaggle.com/stoney71/aflstats) website.There are million different things that can be done with this dataset.At this stage mainly focusing on different teams and player's performance analysis.And also to find interesting correlation between few variables.Hoping to use this dataset for machine learning and performance prediction in future.
 
Each observation (row) is the player’s statistics for one game of AFL Football. Every AFL regular
home & away game and finals series game in the relevant seasons is included.Pre-Season, Reserves and trial games are not included.

Feature columns as per kaggle

Team: The Player’s team or club in that game. Each of the 16 AFL clubs are included.

Player: The player in the format: “Last, First”.

D.O.B: The player’s Date of Birth

Height: The player’s height in cm.

Weight: The player’s weight in Kg, as recorded once in www.footywire.com and not necessarily at
the time the game was played. This feature will be the same for a given player in every observation.

Position: The player’s recognised field position as recorded once in www.footywire.com and not
necessarily where they played in the game.

Season: The season or Year the game was played in.

Round: The Round or final of the game in the given Season, eg R1, R2, R3 is Round 1, Round 2, Round
3 etc. EF = Elimination Final, GF = Grand Final, PF = Preliminary Final, QF = Qualifying Final, SF = Semi
Final.

Date: The Date of the game.

Score: The player’s team score in that game.

Margin: The player’s team margin against the Opposition team in that game. Negative number
represents a losing margin.

WinLoss: Whether the player’s team won, lost or drew the game (W/L/D).

Opposition: The Opposition team in that game.

Venue: The stadium where the game was played. Traditional stadium names are used rather than
sponsor’s naming rights. 

Remaining Columns: The individual recorded statistics for the Player in that game.

Sources
D.O.B., Height, Weight & Position from www.footywire.com
All other data from http://afltables.com

 
All these data is stored in one single csv file.The original data [Australian_Football_League_Database.csv](https://raw.githubusercontent.com/thushara-lakshmanan/python-intro/master/data/Australian_Football_League_Database.csv)- is saved  in [data](https://github.com/thushara-lakshmanan/python-intro/tree/master/data) folder.There is also a cleaned version called [AFL_Ready.csv](https://raw.githubusercontent.com/thushara-lakshmanan/python-intro/master/data/AFL_Ready.csv) in the same folder.

[**The Jupyter notebook for this analysis is saved as mini_assessment_week6_TL.ipynb**](https://github.com/thushara-lakshmanan/python-intro/blob/master/lesson_6/mini-assessment_6/mini_assessment_week6_TL.ipynb)

Table of contents

1. Load Data
2. Inspect Data
3. Clean & Prepare Data
4. Exploratory Data Analysis

    4.1. By Team
    
    4.2. By Player
    
5. Summary
6. Future Work

Note: As data was in good condition not much cleaning was needed.Data was missing for West Coast & Collingwood QF-2018 and Melbourne & Geelong EF-2018 and it was replaced as per [wikipedia](https://en.wikipedia.org/wiki/2018_AFL_finals_series).Couple of unwanted columns are dropped and few new columns are added.

This dataset really helped to get more insight on team and player's performance.