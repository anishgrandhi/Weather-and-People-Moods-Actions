# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:01:49 2017
Reference - Professor Gene Moo Lee's class codes
@author: Anish
"""

from twython import TwythonStreamer
import time
#import sys
import json

bCount, wCount, hCount, rCount, fCount = 0,0,0,0,0
class MyStreamer(TwythonStreamer):
    '''our own subclass of TwythonStremer'''
    # overriding
    def on_success(self, data):
        global bCount, wCount, hCount, rCount, fCount
        if 'lang' in data and data['lang'] == 'en'and 'bought' in data['text'].lower():
            bCount+=1
            if bCount <= 100000:
                print ("bCount: {}".format(bCount))
                self.store_json(data,"bought")
            else:
                self.disconnect()
#            print ("Bought tweet!! {}".format(data['text'].encode('utf-8')))
        if 'lang' in data and data['lang'] == 'en'and ('workout' or 'cardio' or 'gym' or 'exercise' or 'jogging') in data['text'].lower():
            wCount+=1
            if wCount <= 100000:
                print ("wCount: {}".format(wCount))
                self.store_json(data,"workout")
            else:
                self.disconnect()
#            print ("Workout!! {}".format(data['text'].encode('utf-8')))
        if 'lang' in data and data['lang'] == 'en'and ('happy' or 'excited' or 'joy') in data['text'].lower():
            hCount+=1
            if hCount <= 100000:
                print ("hCount: {}".format(hCount))
                self.store_json(data,"happy")
            else:
                self.disconnect()
#            print ("Happy!! {}".format(data['text'].encode('utf-8')))
        if 'lang' in data and data['lang'] == 'en'and ('beach' or 'ride' or 'outing' or 'sunny' or 'going out') in data['text'].lower():
            rCount+=1
            if rCount <= 100000:
                print ("rCount: {}".format(rCount))
                self.store_json(data,"ride")
            else:
                self.disconnect()
        if 'lang' in data and data['lang'] == 'en'and ('food' or 'restaurent' or 'eating out' or 'burger' or 'pizza' or 'cheese') in data['text'].lower():
            fCount+=1
            if fCount <= 100000:
                print ("fCount: {}".format(fCount))
                self.store_json(data,"food")
            else:
                self.disconnect()
        
    # overriding
    def on_error(self, status_code, data):
        print (status_code, data)
        self.disconnect()

    def store_json(self,data,ttype):
        if ttype == "bought":
            with open('tweet_stream_bought_NC.json', 'a') as f:	
                json.dump(data, f)
                f.write("\n")
        elif ttype == "workout":
            with open('tweet_stream_workout_NC.json', 'a') as f:	
                json.dump(data, f)
                f.write("\n")
        elif ttype == "happy":
            with open('tweet_stream_happy_NC.json', 'a') as f:	
                json.dump(data, f)
                f.write("\n")
        elif ttype == "ride":
            with open('tweet_stream_ride_NC.json', 'a') as f:	
                json.dump(data, f)
                f.write("\n")
        elif ttype == "food":
            with open('tweet_stream_food_NC.json', 'a') as f:	
                json.dump(data, f)
                f.write("\n")
#    def sendemail(count): 
#        fromaddr = "remind.py@gmail.com"
#        toaddr = "anish12392@gmail.com"
#        msg = MIMEMultipart()
#        msg['From'] = fromaddr
#        msg['To'] = toaddr
#        msg['Subject'] = "Tw Notification"
#         
#        body = ("No. of tweets stopped at - {}".format(count))
#        msg.attach(MIMEText(body, 'plain'))
#         
#        server = smtplib.SMTP('smtp.gmail.com', 587)
#        server.starttls()
#        server.login(fromaddr, "mailremind")
#        text = msg.as_string()
#        server.sendmail(fromaddr, toaddr, text)
#        server.quit()
        
if __name__ == '__main__':

    with open('your_twitter_credentials.json', 'r') as f:
        credentials = json.load(f)

    # create your own app to get consumer key and secret
    CONSUMER_KEY = credentials['CONSUMER_KEY']
    CONSUMER_SECRET = credentials['CONSUMER_SECRET']
    ACCESS_TOKEN = credentials['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = credentials['ACCESS_TOKEN_SECRET']
        
    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET,retry_in=20)

#    if len(sys.argv) > 1:
#        keyword = sys.argv[1]
#    else:
#        keyword = 'trump'

    #Put longitude and then latitude of SW point and then long and lat of NE point of the box!!
    
    
    #stream.statuses.filter(track=keyword)
    
    for i in range (0,20):
        try:
            stream.statuses.filter(locations=[-75.59,38.45,-72.01,40.95])
        except:
            print ("Sleeping for 15 mins. Goodnight sir!")
            time.sleep(900)
            continue
       
