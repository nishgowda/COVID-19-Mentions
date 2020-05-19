import requests
import json
import sys
import os
import datetime 
from progress.bar import Bar
import time
class NY_TIMES():

	def __init__(self):
		self.all_mentions = []
		self.key = 't4IhXf8GakTGmg1VzX1jGRIdk21cWnpd'
		self.file_name = ""
		self.dir = ""
		self.current_date = datetime.datetime.now()


	# FUNCTION TO CREATE A TEXT FILE AND ALLOW US TO WRITE OUR CONTENT INTO IT
	def write_into_text(self, text):
		path = self.dir
		if not os.path.exists(path):
			os.makedirs(path)
		filename = self.file_name + '.txt'
		bar = Bar('Processing', max = len(text))
		for i in range(100):
			with open(os.path.join(path, filename), 'w+') as temp_file:
				temp_file.write(str(text))
			bar.next()
		bar.finish()
		print('Done')


	# ACCESS THE NY TIMES API TO TRAVERSE THROUGH THE KEYWORDS OF ARCHIVED NY TIMES ARTICLE UP UNTIL THE CURRENT MONTH
	def keywords(self):
		print('...checking keywords')
		num_months = 1
		while(num_months != (self.current_date.month+1)):
			endpoint_url = f'https://api.nytimes.com/svc/archive/v1/2020/{num_months}.json?api-key={self.key}'
			r = requests.get(endpoint_url)
			articles = r.json()
			for words in articles['response']['docs'][0]['keywords']:
				if 'COVID' in words['value'] or 'Coronavirus' in words['value']:
					if words['value'] not in self.all_mentions:
						self.all_mentions.append(words['value'])
			num_months+=1

		#self.write_into_text(self.all_mentions)
	# ACCESS THE NY TIMES API TO TRAVERSE THROUGH THE MAIN HEADLINES OF ARCHIVED NY TIMES ARTICLE UP UNTIL THE CURRENT MONTH
	def mains(self):
		print('...checking headlines')
		num_months = 1
		while(num_months != (self.current_date.month + 1)):
			endpoint_url = f'https://api.nytimes.com/svc/archive/v1/2020/{num_months}.json?api-key={self.key}'
			r = requests.get(endpoint_url)
			articles = r.json()
			
			for words in articles['response']['docs']:
				main = (words['headline']['main'])
				if 'COVID' in main or 'Coronavirus' in main:
					if main not in self.all_mentions: 
						self.all_mentions.append(main)
			num_months+=1
		#self.write_into_text(self.all_mentions)
	# ACCESS THE NY TIMES API TO TRAVERSE THROUGH THE NEWS DESK OF IDEAS OF ARCHIVED NY TIMES ARTICLE UP UNTIL THE CURRENT MONTH
	def news_desk(self):
		print('...checking news desk')
		num_months = 1
		while(num_months != (self.current_date.month+1)):
			endpoint_url = f'https://api.nytimes.com/svc/archive/v1/2020/{num_months}.json?api-key={self.key}'
			r = requests.get(endpoint_url)
			articles = r.json()

			for words in articles['response']['docs']:
				desk = words['news_desk']
				if 'COVID' in desk or 'Coronavirus' in desk:
					if desk not in self.all_mentions:
						self.all_mentions.append(desk)
			num_months += 1
		#self.write_into_text(self.all_mentions)

