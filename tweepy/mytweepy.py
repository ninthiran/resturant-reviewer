# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 12:27:28 2018

@author: naveen
"""

import tweepy
from tweepy import Stream
from tweepy import StreamListener 
from tweepy import OAuthHandler
import json
import csv
from local_config import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


#

csvFile = open('tweeter_Tweepy.csv', 'w', newline='',encoding='utf-8')

csvWriter = csv.writer(csvFile)
csvWriter.writerow(["id","text","lon","lat"])

a= []

for tweet in tweepy.Cursor(api.search,q="Restaurant london",count=500,
                           lang="en",
                           since="2017-08-01").items(10000):
    
    if (tweet.coordinates is not None):
        csvWriter.writerow([tweet.created_at, tweet.text,tweet.coordinates])
    
csvFile.close()