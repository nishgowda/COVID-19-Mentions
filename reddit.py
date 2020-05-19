import requests
import json
import sys
import os
import praw

class Reddit:
	def __init__(self):
		self.all_mentions=[]
		self.client_id = ''
		self.client_secret= ''
		self.user_agent=''
		self.file_name = ''
		self.dir = ''
		self.reddit = praw.Reddit(client_id=self.client_id,client_secret=self.client_secret,user_agent=self.user_agent)
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

		topics = ['Coronavirus', 'COVID19']
		while(len(topics) > 0):
			topic = topics[0]
			subreddit = self.reddit.subreddit(str(topic))

			for submission in subreddit.top():
				if submission.title not in self.all_mentions:
					self.all_mentions.append(submission.title)
			topics.pop(0)

	def aggregate_comments(self):
		print('...checking comments')
		topics = ['Coronavirus', 'COVID19']
		while(len(topics) > 0):
			topic = topics[0]
			subreddit = self.reddit.subreddit(str(topic))
			for subreds in subreddit.top():
				submissions = self.reddit.submission(subreds.id)
				submissions.comments.replace_more(limit=0)
				for comment in submissions.comments:
					if 'COVID' in comment.body or 'Coronavirus' in comment.body:
						self.all_mentions.append(comment.body)
			topics.pop(0)
		#self.write_into_text(self.all_mentions)
