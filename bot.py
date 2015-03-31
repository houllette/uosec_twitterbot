#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tweets a .txt file line by line, waiting a set amount of time between each tweet.
# Functionality will soon change this so it tweets different things based on the date.
# This script must be running all the time, it will be run on Google Scripts, this would
# ideally work as a cron task.

import tweepy, time, datetime

CONSUMER_KEY = 'XXXX' #requires info from twitter
CONSUMER_SECRET = 'XXXX'
ACCESS_KEY = 'XXXX'
ACCESS_SECRET = 'XXXX'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

now = datetime.datetime.now()
day = now.strftime("%A")

f = ""
phrase = ""

if day == "Tauesday":
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