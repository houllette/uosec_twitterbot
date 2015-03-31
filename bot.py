#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tweets a .txt file line by line, waiting a set amount of time between each tweet.
# Functionality will soon change this so it tweets different things based on the date.
# This script must be running all the time, it will be run on Google Scripts, this would
# ideally work as a cron task.

import tweepy, time, datetime

CONSUMER_KEY = '15VqSq52QpjVb0VXQ9aTUVFIo'
CONSUMER_SECRET = 'EAt5Ikt1gJQ0O0UpjySOqymm8lxH0WknejrmCRGIyMgtd0Qnzv'
ACCESS_KEY = '3118658258-YZAW8h9Lr1GOHx5RlDxSAGjRFWs85fUvu7yEHGy'
ACCESS_SECRET = 'jEsxMDjczLQjj6F42fM2caB3I0WjcTPGQlQ0y9hwPPJez'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

now = datetime.datetime.now()
day = now.strftime("%A")

f = ""
phrase = ""

if day == "Tuesday":
	filename = open('tuesday.txt','r')
	f = filename.readlines()
	filename.close()
	for line in f:
		for x in range(0,40):
			phrase += line[x]
		phrase += " ("+time.strftime("%m/%d/%Y")+") "
		length = len(line)
		for x in range(41,length):
			phrase += line[x]
	api.update_status(status=phrase)
	print phrase
elif day == "Thursday":
	filename = open('thursday.txt','r')
	f = filename.readlines()
	filename.close()
	for line in f:
		for x in range(0,36):
			phrase += line[x]
		phrase += " ("+time.strftime("%m/%d/%Y")+") "
		length = len(line)
		for x in range(37,length):
			phrase += line[x]
	api.update_status(status=phrase)
	print phrase
elif day == "Saturday":
	filename = open('saturday.txt','r')
	f = filename.readlines()
	filename.close()
	for line in f:
		for x in range(0,29):
			phrase += line[x]
		phrase += " ("+time.strftime("%m/%d/%Y")+") "
		length = len(line)
		for x in range(30,length):
			phrase += line[x]
	api.update_status(status=phrase)
	print phrase
