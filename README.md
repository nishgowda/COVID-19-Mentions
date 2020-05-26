# COVID-19-Mentions
### HOW?
By fetching data from various news outlets, the program determines how many instances of COVID-19 related mentions occured from January 2020 to the current month using archived news articles and posts. Currently, this program only accesses data from the NY Times, The Guardian, CNN, Reddit, and The Wall Street Journal. The program searches through this data, records all of it by creating or updating a local text file, and creates a model through matplot for visualization. 
### How to Run:
- You must have valid credentials for these select API's : NY Times, The Guardian, Reddit, and the News API. These can be found on their websites, just create an account and replace the credentials with yours. Be aware, that if you run the program with the NY Times model, then it will not work. This is because they place a limit on the number of requests you can make per minute. To solve this, just email them with a request to increase this rate. Also please note that if you run this while writing the content to your local text file, it will be a VERY large file. 
- cd into directory
## Usage
Example:
```python
  python3 news.py all corona_data ALL_Outlets
```
Command Line Arguments:
 - The news media you wish to scrape:
```
    - all : traverse through all the available news outlets
    - nytimes : traverse the data for just The New York Times
    - guardian : traverse the data for just The Guardian
    - reddit : traverse the data for just Reddit
    - wsj : traverse the data for just The Wall Street Journal
    - cnn: traverse the data for just CNN
```
- The text file you want to write into 
- The directory for your text file (this directory will be placed in the directory of your python file)
### Dependencies/Requirments: 
- requests
- sys
- os
- newsapi
- matplot
- praw

### The Results:
After the program executes through all the media outlets available, the following percentage model was created. From this data, we can see that The Guardian and New York Times accumulated more than 85% combined of mentions in the media from January to today (5/21/20). It is important to note however, that this data is obvioulsy not a 100% accurate representation of what's being mentioned in the news. Due to limitations with several API's and the sheer number of articles to search through, the results will obviously not account for all mentions of COVID-19 related topics. 
![COVID-mentions-figure](https://github.com/nishgowda/COVID-19-Mentions/blob/master/Covid-mentions-figure.png)
### TO DO:
- [X] Access more news API's
- [X] Increase request rate for NY Times
- [ ] Increase data size for CNN and WSJ
