This is [an example](http://example.com/ "Title") inline link.

#Problem Statement-#
Perform 5 analysis on European Soccer Database.
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

*  Analysis1.py: In year 2013 and 2014 those player with highest overall rating used which foot left or right. This categories the player in left and right preferred foot in the year 2013 and 2014.Result set has top 8 players each.
*  Analysis2.py: Country or League grouped by season and stage and compare home team goal and away team goal.
*  Analysis3.py: FOR EPL, get the Team Attributes for each team over the seasons present in the Match.
*  Analysis4.py: In LA LIGA, Stat of each of the team over the period of years
*  Analysis5.py: Combine Player and player attributes to compare the attributes like balance, shot power, stamina and strength and sort it by age of the players

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
