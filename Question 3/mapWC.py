#!/usr/bin/env python

import sys
import string
import json

tweets=[]
for line in sys.stdin:
  tweets.append(json.loads(line))
for tweet in tweets:
  user=tweet['user']
  screen_name=user['screen_name']
  content=tweet['text']
  content_length = len(content)  
  print '%s\t%s' % (screen_name,content_length)
