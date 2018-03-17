#!/usr/bin/env python

import sys
import string
import json

tweets=[]

for line in sys.stdin:
  tweets.append(json.loads(line))
  
year_list=[]
count=1

for tweet in tweets:
  user=tweet['user']
  screen_name=user['screen_name']
  if(screen_name=='PrezOno'):
    day=tweet['created_at'].split(' ')[0]
    print '%s\t%s' % (day, 1)

