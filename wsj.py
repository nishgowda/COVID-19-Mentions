import requests
import sys
import json
import os
from newsapi import NewsApiClient
import datetime  
class WSJ():

    def __init__(self):
        self.key = ''
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
        current_date = datetime.datetime.now()
        num_months = 0
        print('...searching recent articles')
        topics = ['Coronavirus', 'COVID-19', 'Pandemic']
        newsapi = NewsApiClient(api_key=self.key)
        while (len(topics) > 0):
            topic = topics[0]
            while(num_months < current_date.month):
                to_date = f'{current_date.year}-0{current_date.month - num_months}-{current_date.day}'
                from_date = f'{current_date.year}-0{current_date.month - 1}-{current_date.day}'
                articles = newsapi.get_everything(q=f'{topic}',
                                                      sources='The-Wall-Street-Journal',
                                                      from_param=f'{from_date}',
                                                      to=f'{to_date}',
                                                      language='en',)
                for titles in articles['articles']:
                    if titles['title'] not in self.all_mentions:
                        self.all_mentions.append(titles['title'])
                num_months+=1
            topics.pop(0)
