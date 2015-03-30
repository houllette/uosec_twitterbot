#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tweets a .txt file line by line, waiting a set amount of time between each tweet.
# Functionality will soon change this so it tweets different things based on the date.
# This script must be running all the time, it will be run on Google Scripts, this would
# ideally work as a cron task.

import tweepy, time

CONSUMER_KEY = 'XXXXX'
CONSUMER_SECRET = 'XXXXX'
ACCESS_KEY = 'XXXXX'
ACCESS_SECRET = 'XXXXX'
auth = tweepy.0AuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open('tuesday.txt','r')
f = filename.readlines()
filename.close()

for line in f:
	api.update_status(line)
	print line
	time.sleep(3600) # Sleeps for 1 hour