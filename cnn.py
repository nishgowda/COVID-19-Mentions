import requests
import sys
import json
import os
from newsapi import NewsApiClient

class CNN():
	def __init__(self):
		self.key = '5cae8a19ef62424788815c036b9e2e44'
		self.all_mentions = []
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

	def everything(self):
		print('...searching all off CNN')
		topics = ['Coronavirus', 'COVID-19', 'Pandemic']
		newsapi = NewsApiClient(api_key=self.key)
		while (len(topics) > 0):
			topic = topics[0]
			articles = newsapi.get_everything(q=f'{topic}',
		                                          sources='CNN',
		                                          from_param='2020-04-18',
		                                          to='2020-05-18',
		                                          language='en',)
			for titles in articles['articles']:
				self.all_mentions.append(titles['title'])
			topics.pop(0)
		self.write_into_text(self.all_mentions)

def main():
	cnn = CNN()
	cnn.file_name = sys.argv[1]
	cnn.dir = sys.argv[2]
	cnn.everything()
	print('Total mentions: ' + str(len(cnn.all_mentions)))
	print('Saved content to  ' + cnn.file_name + ' at ' + cnn.dir)

main()
