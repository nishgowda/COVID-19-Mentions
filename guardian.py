import requests
import sys
import json
import os

class Guardian():
	def __init__(self):
		self.key = ''
		self.mentions = []
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

		endpoint_url = f'http://content.guardianapis.com/search?q=coronavirus'
		payload = {'api-key':              self.key, 'show-fields':          'all'}
		r = requests.get(endpoint_url, params=payload)
		articles = r.json()
		self.num_articles += articles['response']['total']
		self.mentions.append("Page Titles\n")
		for words in articles['response']['results']:
			self.mentions.append(words['webTitle'])
		self.mentions.append("Page URLS\n")
		for urls in articles['response']['results']:
			self.mentions.append(words['webUrl'])
		self.write_into_text(self.mentions)
def main():
	g = Guardian()
	g.file_name = sys.argv[1]
	g.dir = sys.argv[2]
	g.searches()
	print('There were a total of : ' + str(g.num_articles) + ' mentioned')
main()


