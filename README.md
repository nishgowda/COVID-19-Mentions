# COVID-19-Mentions
### HOW?
By fetching data from various news outlets, the program determines how many instances of COVID-19 related mentions occured from January 2020 to the current month using archived news articels. Currently, this program only accesses data from the NY Times, The Guardian, CNN, Reddit, and The Wall Street Journal but I plan to support other outlets as well.

### How to Run:
- cd into directory
- python3 main.py < news outlet > < file name > < directory name > (note the this directory will be made in the directory of your python file)

### Dependencies
- requests
- json
- sys
- os
- newsapi

### The Results:
After the program executes through all the media outlets available, the following percentage model was created. From this data, we can see that the New York Times accumulated more than 80% of mentions in the media from January to this day (5/19/20). It is important to note however, that this data is obvioulsy not a 100% accurate representation of what's being mentioned in the news. Due to limitations with several API's and the sheer number of articles to search through, the results will obviously not account for all mentions of COVID-19 related topics.
![Covid-Mentions](https://github.com/nishgowda/COVID-19-Mentions/blob/master/Covid-Mentions.png)
### TO DO:
- [ ] Access more news API's
- [X] Increase request rate for NY Times
