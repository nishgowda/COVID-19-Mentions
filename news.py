import sys
import os
import json
from nytimes import NY_TIMES
from cnn import CNN
from guardian import Guardian
from reddit import Reddit
from wsj import WSJ
from progress.bar import Bar
import time
import matplotlib.pyplot as plt

class News:
	def __init__(self):
		self.data = []
		self.data_labels = []
		self.total_mentions = 0
		self.mention_content = []
		self.application = ''
		self.file_name = ''
		self.dir = ''
	def write_into_text(self, text):
		path = self.dir
		if not os.path.exists(path):
			os.makedirs(path)
		filename = self.file_name + '.txt'
		bar = Bar('Writing into Text', max = 100, suffix='%(percent)d%%')
		for i in range(100):
			with open(os.path.join(path, filename), 'a') as temp_file:
				time.sleep(0.1)
				temp_file.write(str(text))
			bar.next()
		bar.finish()
		print('Done')

# Function to executing all functions from the created modules and gathering the total data
	def execute(self):
		nytimes = NY_TIMES()
		cnn = CNN()
		guardian = Guardian()
		reddit = Reddit()
		wsj = WSJ()
		if self.application == 'all':
			print('...searching The New York Times')
			nytimes.search()
			nytimes.keywords()
			nytimes.mains()
			nytimes.top_stories()
			self.write_into_text(nytimes.all_mentions)
			print('...searching CNN')
			cnn.everything()
			self.write_into_text(cnn.all_mentions)
			print('...searching The Guardian')
			guardian.searches()
			self.write_into_text(guardian.num_articles)
			print('...searching Reddit')
			reddit.aggregate_submissions()
			reddit.aggregate_comments()
			self.write_into_text(reddit.all_mentions)
			print('...searching The Wall Street Journal')
			wsj.everything()
			self.write_into_text(wsj.all_mentions)
			self.total_mentions = (nytimes.total_mentions) + len(cnn.all_mentions) + (guardian.num_articles) + len(reddit.all_mentions) + len(wsj.all_mentions)
			print('There are a total of ' + str((self.total_mentions)) + ' mentions')
			print('The New York Times had ' + str((nytimes.total_mentions)) + ' mentions')
			print('CNN had ' + str(len(cnn.all_mentions)) + ' mentions')
			print('The Guardian had ' + str(guardian.num_articles) + ' mentions')
			print('Reddit had ' + str(len(reddit.all_mentions)) + ' mentions')
			print('The Wall Street Jornal had ' + str(len(wsj.all_mentions)) + ' mentions')
			print('...Generating your model')
			# Send the data to create the matplot graph
			self.data = [(nytimes.total_mentions), len(cnn.all_mentions), (guardian.num_articles) , len(reddit.all_mentions) , len(wsj.all_mentions)]
			self.data_labels = ['The New York Times', 'CNN', 'The Guardian', 'Reddit', 'The Wall Street Journal']
			plt.pie(self.data, labels = self.data_labels, autopct = '%1.1f%%')
			plt.title('COVID-19 Mentions')
			plt.axis('equal')
			plt.show()
		elif self.application == 'nytimes':
			#nytimes.search()
			#nytimes.keywords()
			#nytimes.mains()
			nytimes.top_stories()
			self.write_into_text(nytimes.all_mentions)
			self.total_mentions = nytimes.total_mentions
			print('The New York Times had ' + str(nytimes.total_mentions) + ' mentions')
		elif self.application == 'guardian':
			guardian.searches()
			self.write_into_text(guardian.all_mentions)
			self.total_mentions = guardian.num_articles
			print('The Guardian had ' + str(len(guardian.num_articles)) + ' mentions')
		elif self.application == 'cnn':
			cnn.everything()
			self.write_into_text(cnn.all_mentions)
			self.total_mentions = len(cnn.all_mentions)
			print('CNN had ' + str(cnn.all_mentions) + ' mentions')
		elif self.application == 'reddit':
			reddit.aggregate_submissions()
			reddit.aggregate_comments()
			self.write_into_text(reddit.all_mentions)
			self.total_mentions = len(reddit.all_mentions)
			print('Reddit had ' + str(len(reddit.all_mentions)) + ' mentions')
		elif self.application == 'wsj':
			wsj.everything()
			self.write_into_text(wsj.all_mentions)
			self.total_mentions = len(wsj.all_mentions)
			print('The Wall Street Journal had ' + str(len(wsj.all_mentions)) + ' mentions')
		else:
			print('Not a valid option')



if __name__ == "__main__":
	news = News()
	news.application = sys.argv[1]
	news.file_name = sys.argv[2]
	news.dir = sys.argv[3]
	news.execute()
