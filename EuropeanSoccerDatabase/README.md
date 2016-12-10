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

##Analysis:##

*  Analysis1.ipynb: In year 2013 and 2014 those player with highest overall rating used which foot left or right. This gives the player according to the left and right preferred foot in the year 2013 and 2014.Result set has top 8 players each.
*  Analysis2.ipynb: Country or League grouped by season and stage and compare home team goal and away team goal.
     ![Alt text](https://github.com/Pragya1025/Python4DataAnalysis/blob/master/EuropeanSoccerDatabase/Graph/output2/2008-2009.png)
*  Analysis3.ipynb: FOR EPL, get the Team Attributes for each team over the seasons present in the Match.
       ![Alt text](https://github.com/Pragya1025/Python4DataAnalysis/blob/master/EuropeanSoccerDatabase/Graph/output3/Arsenal%20%20Stats.png)
*  Analysis4.ipynb: In LA LIGA, Stat of each of the team over the period of years
     ![Alt text](https://github.com/Pragya1025/Python4DataAnalysis/blob/master/EuropeanSoccerDatabase/Graph/output4/Athletic%20Club%20de%20Bilbao%20Match%20%20Stats.png)
*  Analysis5.ipynb: Combine Player and player attributes to compare the attributes like balance, shot power, stamina and strength and sort it by age of the players
     ![Alt text](https://github.com/Pragya1025/Python4DataAnalysis/blob/master/EuropeanSoccerDatabase/Graph/output5.png)

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

##Contributing Points:##
* Graph for analysis2,3 and 4 gets stored in a separate  folder
* There is no graph for analysis 1 as it gives basic stats only
* Analysis 5 has its plot shown while it runs it does not get stored separately
* Output of each analysis gets stored in a CSV file in xls format.

