# -*- coding: utf-8 -*-
"""
Created on Tue May 09 17:47:59 2017
References-
https://chrisalbon.com/machine-learning/linear_regression_scikit-learn.html
http://blog.coderscrowd.com/twitter-hashtag-data-analysis-with-python/
@author: Anish
"""

import json
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import time

import matplotlib.pyplot as plt


#Extracting data from json files
data_twitter = []
tweets_file = open("../tweet_stream_happy_CA.json", "r")
#tweets_file = open("tweet_stream_happy_CA.json", "r")
#tweets_file = open("tweet_stream_food_CA.json", "r")
#tweets_file = open("tweet_stream_food_NJ.json", "r")
#tweets_file = open("tweet_stream_ride_CA.json", "r")
#tweets_file = open("tweet_stream_ride_NJ.json", "r")
#tweets_file = open("tweet_stream_bought_CA.json", "r")
#tweets_file = open("tweet_stream_bought_NJ.json", "r")
#tweets_file = open("tweet_stream_workout_CA.json", "r")
#tweets_file = open("tweet_stream_workout_NJ.json", "r")
for line in tweets_file:
    try:
        data_twitter.append(json.loads(line))
    except:
        continue

#Load the data into pandas
tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'].encode('utf-8'), data_twitter)
tweets['created_at'] = map(lambda tweet: time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')), data_twitter)

#Clearing the memory
del data_twitter[:]

#Drop irrelevant tweets
to_drop = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','professionals','Sibling','sibling','SIBLING']
#to_drop = ['hire','hiring','job']

tweets = tweets[~tweets['text'].str.contains('|'.join(to_drop))]

#Count the number of tweets with respect to time
df = pd.DataFrame()
df['number_tweets'] = tweets['created_at'].value_counts()
df['date'] = df.index
print df.head()

#Split the date, count the number of tweets per day
days = [item.split(" ")[0] for item in df['date'].values]
df['days'] = days
grouped_tweets = df[['days', 'number_tweets']].groupby('days')
tweet_number = grouped_tweets.sum()
tweet_number['days']= tweet_number.index

print "tweetNumber: ",tweet_number

#Plot graphs
fig = plt.figure(figsize=(10,10),dpi=100,facecolor='white')
ax = plt.subplot(111)
x_pos = np.arange(len(tweet_number['days'].values))
ax.bar(x_pos, tweet_number['number_tweets'].values, align='center',color=['brown'])
ax.set_xticks(x_pos)
ax.set_facecolor('white')

ax.set_title('Number of people Happy - CA')
ax.set_ylabel("number tweets")
ax.set_xticklabels(tweet_number['days'].values,rotation='vertical')
fig.savefig('Number of people Happy - CA.png')