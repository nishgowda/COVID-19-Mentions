import requests
import json
import sys
import os

class Covid_Tracker():

	def __init__(self):
		self.all_mentions = []
		self.key = 'KEY'
		self.file_name = ""
		self.dir = ""

	# FUNCTION TO CREATE A TEXT FILE AND ALLOW US TO WRITE OUR CONTENT INTO IT
	def write_into_text(self, text):
		path = self.dir
		if not os.path.exists(path):
			os.makedirs(path)
		filename = self.file_name + '.txt'
		with open(os.path.join(path, filename), 'w+') as temp_file:
			temp_file.write(str(text))
		print('Done') 
	# ACCESS THE NY TIMES API TO TRAVERSE THROUGH THE KEYWORDS OF ARCHIVED NY TIMES ARTICLE UP UNTIL THE CURRENT MONTH
	def keywords(self):
		print('...checking keywords')
		num_months = 1
		self.all_mentions.append("ALL KEYWORDS:\n")
		while(num_months != 6):
			endpoint_url = f'https://api.nytimes.com/svc/archive/v1/2020/{num_months}.json?api-key={self.key}'
			r = requests.get(endpoint_url)
			articles = r.json()
			for words in articles['response']['docs'][0]['keywords']:
				if 'COVID' in words['value'] or 'Coronavirus' in words['value']:
					self.all_mentions.append(words['value'])
			num_months+=1

		self.write_into_text(self.all_mentions)
	# ACCESS THE NY TIMES API TO TRAVERSE THROUGH THE MAIN HEADLINES OF ARCHIVED NY TIMES ARTICLE UP UNTIL THE CURRENT MONTH
	def mains(self):
		print('...checking headlines')
		num_months = 1
		self.all_mentions.append("ALL MAIN:\n")
		while(num_months != 6):
			endpoint_url = f'https://api.nytimes.com/svc/archive/v1/2020/{num_months}.json?api-key={self.key}'
			r = requests.get(endpoint_url)
			articles = r.json()
			
			for words in articles['response']['docs']:
				main = (words['headline']['main'])
				if 'COVID' in main or 'Coronavirus' in main: 
					self.all_mentions.append(main)
			num_months+=1
		self.write_into_text(self.all_mentions)
	# ACCESS THE NY TIMES API TO TRAVERSE THROUGH THE NEWS DESK OF IDEADS OF ARCHIVED NY TIMES ARTICLE UP UNTIL THE CURRENT MONTH
	def news_desk(self):
		print('...checking news desk')
		self.all_mentions.append("NEWS DESK\n")
		num_months = 1
		while(num_months != 6):
			endpoint_url = f'https://api.nytimes.com/svc/archive/v1/2020/{num_months}.json?api-key={self.key}'
			r = requests.get(endpoint_url)
			articles = r.json()

			for words in articles['response']['docs']:
				desk = words['news_desk']
				if 'COVID' in desk or 'Coronavirus' in desk:
					self.all_mentions.append(desk)
			num_months += 1
		self.write_into_text(self.all_mentions)


def main():
	t = Covid_Tracker()
	t.file_name = sys.argv[1]
	t.dir = sys.argv[2]
	t.keywords()
	t.mains()
	t.news_desk()
	print("All mentions in the NY Times: " + len(t.all_mentions))

main()
