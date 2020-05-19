import requests
import sys
import json
import os

class Guardian():
	def __init__(self):
		self.key = 'eeade75e-0f7e-4e67-a641-0b17f7ca2b54'
		self.all_mentions = []
		self.num_articles = 0
		self.file_name = ""
		self.dir = ""
	def write_into_text(self, text):
		path = self.dir
		if not os.path.exists(path):
			os.makedirs(path)
		filename = self.file_name + '.txt'
		with open(os.path.join(path, filename), 'w+') as temp_file:
			temp_file.write(str(text))
		print('Done') 

	def searches(self):
		print('...checking all searches')
		topics = ['coronavirus', 'covid-19']
		while(len(topics) > 0):
			topic = topics[0]
			endpoint_url = f'http://content.guardianapis.com/search?q={topic}'
			payload = {'api-key':              self.key, 'show-fields':          'all'}
			r = requests.get(endpoint_url, params=payload)
			articles = r.json()
			self.num_articles += articles['response']['total']
			for words in articles['response']['results']:
				if words['webTitle'] not in self.all_mentions:
					self.all_mentions.append(words['webTitle'])
			topics.pop(0)

		#self.write_into_text(self.all_mentions)



