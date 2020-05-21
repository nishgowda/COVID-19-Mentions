import requests
import json
import sys
import os
import praw

class Reddit:
	def __init__(self):
		self.all_mentions=[]
		self.client_id = 'client_id'
		self.client_secret= 'client_secret'
		self.user_agent='user_agent'
		self.file_name = ''
		self.dir = ''
		self.reddit = praw.Reddit(client_id=self.client_id,client_secret=self.client_secret,user_agent=self.user_agent)
		self.total_mentions =0
	def write_into_text(self, text):
		path = self.dir
		if not os.path.exists(path):
			os.makedirs(path)
		filename = self.file_name + '.txt'
		with open(os.path.join(path, filename), 'w+') as temp_file:
			temp_file.write(str(text))
		print('Done')
# Gathering all the subissions from reddit and appending all mentions of COVID-19 in various subreddits to all_mentions
	def aggregate_submissions(self):
		print('...checking submissions')

		topics = ['Coronavirus', 'COVID19','COVID','COVID19positive']
		while(len(topics) > 0):
			topic = topics[0]
			subreddit = self.reddit.subreddit(str(topic))
			for submission in subreddit.top():
				if submission.title not in self.all_mentions:
					self.all_mentions.append(submission.title)
			topics.pop(0)

	def aggregate_comments(self):
		print('...checking comments')
		topics = ['Coronavirus', 'COVID19','COVID','COVID19positive']
		while(len(topics) > 0):
			topic = topics[0]
			subreddit = self.reddit.subreddit(str(topic))
			for comment in subreddit.comments(limit=None):
				self.all_mentions.append(comment.body)
			topics.pop(0)

		#self.write_into_text(self.all_mentions)
