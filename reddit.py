import requests
import json
import sys
import os
import praw

class Reddit:
	def __init__(self):
		self.all_mentions=[]
		self.client_id = 'K7pTKA1qeDOOQg'
		self.client_secret= 'VfFFT1cLOEuaS9jnAl9wywEjdxs'
		self.user_agent='Daily Sieve'
		self.file_name = ''
		self.dir = ''

	def write_into_text(self, text):
		path = self.dir
		if not os.path.exists(path):
			os.makedirs(path)
		filename = self.file_name + '.txt'
		with open(os.path.join(path, filename), 'w+') as temp_file:
			temp_file.write(str(text))
		print('Done')
	
	def aggregate_submissions(self):
		print('...checking submissions')
		reddit = praw.Reddit(client_id=self.client_id,
		                     client_secret=self.client_secret,
		                     user_agent=self.user_agent)
		topics = ['Coronavirus', 'COVID19']
		while(len(topics) > 0):
			topic = topics[0]
			subreddit = reddit.subreddit(str(topic))

			for submission in subreddit.top():
			    self.all_mentions.append(submission.title)
			topics.pop(0)
		self.write_into_text(self.all_mentions)

def main():
	reddit = Reddit()
	reddit.file_name = sys.argv[1]
	reddit.dir = sys.argv[2]
	reddit.aggregate_submissions()
	print("All mentions in the Reddit: " + str(len(reddit.all_mentions)))

main()