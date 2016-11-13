Question:
Use the StackExchange REST API to collect the data for stackoverflow. You are supposed to use at least 3 per-site method. Perform 5 analysis on the data that you collect.

Midterm.py: This script collects the data for stackoverflow from the StackExchange REST API. Import stackexchange from Site and Stackoverflow 
•	Questions_list – It is the list of all the questions
•	User_id-It is the list of all the user id
•	User- It is the dictionary of users
•	Rep_user_map-It is the dictionary of reputation of users
•	Badge_user_map- It is the dictionary of badges of users
•	Badges- It has been classified as gold , silver, bronze
•	Question-It is the dictionary of questions
•	Tags- List of tags

Analysis Performed-
 This script performs 5 analysis:
•	Analysis 1: Get the Questions with tag python and pandas. Parse the body for the responses to collect a list of questions and user_id for the questions. Use the user_id obtained to send a request again to get user profile. Obtain the badges count to determine weightage. Show top questions according to the weightage.
•	Analysis 2: For each of the User ID that you have collected, ping the API to get all the tags that user has identified with. Create a file for each topic, containing user_id,user_name and link to their profile sorted by reputation. For a given topic, what are the top users who have reputation in that topic.
•	Analysis 3: For each of the badge type, find how many users (based on the data you have collected) have badge. 
•	Analysis 4: For each of the question that is asked, find out the
•	tags attached to it. Numbers of answers have been given for each question. For each tag, calculate the number of question asked and how many times it has been answered.
•	Analysis 5: Find out the user whose questions have been downvoted the most.

Dependencies:
•	python: 3.5 or higher (prefered: Python 3.4.4 )

Standard Libraries used:
•	Site
•	Stackoverflow
•	Json
•	os

Key points:
•	A new text file Pandas.text will be created at the in the folder with name "C:\GitHub4Python\Python4DataAnalysis". 40 questions with pandas will be written in it.
•	A new text file Python.text will be created at the in the folder with name "C:\GitHub4Python\Python4DataAnalysis". 40 questions with pandas will be written in it.


