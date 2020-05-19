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

### TO DO:
- [ ] Access more news API's
- [X] Increase request rate for NY Times
