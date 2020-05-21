# COVID-19-Mentions
### HOW?
By fetching data from various news outlets, the program determines how many instances of COVID-19 related mentions occured from January 2020 to the current month using archived news articles and posts. Currently, this program only accesses data from the NY Times, The Guardian, CNN, Reddit, and The Wall Street Journal.
### How to Run:
- You must have valid credentials for these select API's : NY Times, The Guardian, Reddit, and the News API. These can be found on their websites, just create an account and replace the credentials with yours. Be aware, that if you run the program with the NY Times model, then it will not work. This is because they place a limit on the number of requests you can make per minute. To solve this, just email them with a request to increase this rate. Also please not that if you run this while writing the content to your local file, it will be a VERY large file. 
- cd into directory
- python3 news.py < news outlet > < file name > < directory name > (note this directory will be made in the directory of your python file)

### Dependencies/Requirments: 
- requests
- sys
- os
- newsapi
- matplot

### The Results:
After the program executes through all the media outlets available, the following percentage model was created. From this data, we can see that The Guardian accumulated more than 70% of mentions in the media from January to this day (5/19/20). It is important to note however, that this data is obvioulsy not a 100% accurate representation of what's being mentioned in the news. Due to limitations with several API's and the sheer number of articles to search through, the results will obviously not account for all mentions of COVID-19 related topics. 
![COVID-19-Mentions](https://github.com/nishgowda/COVID-19-Mentions/blob/master/Covid-19-Mentions-Figures.png
### TO DO:
- [X] Access more news API's
- [X] Increase request rate for NY Times
