#European Soccer Database Analysis#

![Alt text](https://github.com/Pragya1025/Python4DataAnalysis/blob/master/EuropeanSoccerDatabase/img.jpg)



##Problem Statement-##
Perform 5 analysis on European Soccer Database. The dataset can be accessed from dropbox  [link](https://www.dropbox.com/home/Python%20DataSet/data/ "Dataset") .

##Dataset:##
###The ultimate Soccer database for data analysis###

*  +25,000 matches
*	+10,000 players
*	11 European Countries with their lead championship
*	Seasons 2008 to 2016
*	Players and Teams' attributes* sourced from EA Sports' FIFA video game series, including the weekly updates
*	Team line up with squad formation (X, Y coordinates)
*	Betting odds from up to 10 providers
*	Detailed match events (goal types, possession, corner, cross, fouls, cards etc...) for +10,000 matches

##Sample Dataset##

| Id     | Player_api_id    |player_name | player_fifa_api_id    | birthday    |height | weight     | 
| --------|---------|-------|--------|---------|-------|--------|
|1|505942 | Aaron Appindangoye| 218353 |1992-02-29 00:00:00 |182.88 |187 
|2|55782 |Aaron Cresswell|189615 |1989-12-15 00:00:00 |170.18 |146 
|3|162549 |Aaron Doran |186170 |1991-05-13 00:00:00 |170.18 |163 
|4|30572 | Aaron Galindo |140161 |1982-05-08 00:00:00 |182.88 |198 
|5|23780 |Aaron Hughes |17725 |1979-11-08 00:00:00 |182.88 |154 
|6|27316 | Aaron Hunt |158138 |1986-09-04 00:00:00 |182.88 |161 
|7|564793 | Aaron Kuhl |221280 |1996-01-30 00:00:00 |172.72 |146 
|8|30895 |Aaron Lennon |152747 |1987-04-16 00:00:00 |165.1 |139 
|9|528212|Aaron Lennox|206592 |1993-02-19 00:00:00|190.5 |181 
|10|101042 |Aaron Meijers|188621|  1987-10-28 00:00:00|175.26 |170 


##Analysis:##

*  Analysis1.ipynb: In year 2013 and 2014 those player with highest overall rating used which foot left or right. This gives the player according to the left and right preferred foot in the year 2013 and 2014.Result set has top 8 players each.
###Result Dataset###
| Playr Name | Preferred Foot |Year | Overall Rating    | 
| --------|---------|-------|--------|
|Lionel Messi|left|2014	|94|
|Arjen Robben|left|2014|90|
|Robin van Persie|left|2014|89|
|Iker Casillas|left|2014|88|
|David Silva|left|2014|88|
|Gareth Bale|left|2014|87|
|Mesut Oezil|left|2014|87|
|Juan Mata|left|2014|87|
|Cristiano Ronaldo|right|2014|92|
|Xavi Hernandez|right|2014|90|
|Andres Iniesta|right|2014|90|
|Manuel Neuer|right|2014|90|
|Radamel Falcao|right|2014|90|
|Zlatan Ibrahimovic|right|2014|90|
|Franck Ribery|right|2014|90|
|Luis Suarez|right|2014|89|


*  Analysis2.ipynb: Country or League grouped by season and stage and compare home team goal and away team goal.
     ![Alt text](https://github.com/Pragya1025/Python4DataAnalysis/blob/master/EuropeanSoccerDatabase/Graph/output2/2008-2009.png)
*  Analysis3.ipynb: FOR EPL, get the Team Attributes for each team over the seasons present in the Match.
       ![Alt text](https://github.com/Pragya1025/Python4DataAnalysis/blob/master/EuropeanSoccerDatabase/Graph/output3/Arsenal%20%20Stats.png)
*  Analysis4.ipynb: In LA LIGA, Stat of each of the team over the period of years
     ![Alt text](https://github.com/Pragya1025/Python4DataAnalysis/blob/master/EuropeanSoccerDatabase/Graph/output4/Athletic%20Club%20de%20Bilbao%20Match%20%20Stats.png)
*  Analysis5.ipynb: Combine Player and player attributes to compare the attributes like balance, shot power, stamina and strength and sort it by age of the players
     ![Alt text](https://github.com/Pragya1025/Python4DataAnalysis/blob/master/EuropeanSoccerDatabase/Graph/output5.png)
	 
	  ![Alt text](https://github.com/Pragya1025/Python4DataAnalysis/blob/master/EuropeanSoccerDatabase/Graph/output5_b.png)

##Dependencies:##
* python: 3.5 or higher (prefered: Python 3.5.2 Latest version)

##Standard Libraries used:##
*	datetime
*	csv

##External Libraries used:##
*	matplotlib
*	seaborn
*	pandas
*	numpy

##How to install External Libraries:##
* pip install pandas
* pip install matplotlib
* pip install numpy

##Folder Structure-##
* Dataset- Available by clicking the dropbox link provided
* Analysis- Contains all the five analysis in **ipynb** format
* Output- Saves all the result dataset in *xls* format
* Graph - Saves the graph from analysis 2,3 and 4


##Contributing Points:##
* Graph for analysis2,3 and 4 gets stored in a separate  folder
* There is no graph for analysis 1 as it gives basic stats only
* Analysis 5 has its plot shown while it runs it does not get stored separately
* Output of each analysis gets stored in a CSV file in xls format.

