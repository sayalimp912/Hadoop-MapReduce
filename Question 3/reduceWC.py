#!/usr/bin/env python

import sys
import string

word_count = 0
old_word = None
count=0
other_avg=0
PrezOno_avg=0
avg_per_user = {}
for line in sys.stdin:
  (key,val) = line.strip().split('\t',1) 
  user_name, tweet_length = line.split('\t')

  if user_name in avg_per_user:
    avg_per_user[user_name].append(int(tweet_length))
  else:
    avg_per_user[user_name] = []
    avg_per_user[user_name].append(int(tweet_length))
                
for user_name in avg_per_user.keys():
  avg_tweet_length = sum(avg_per_user[user_name])*1.0 / len(avg_per_user[user_name])
  if user_name == 'PrezOno':
    PrezOno_avg = avg_tweet_length
    print '%.2f'% (PrezOno_avg)
  else:
    other_avg += avg_tweet_length
    
avg_other_users = other_avg/(len(avg_per_user.keys()) -1)
print '%.2f'% (PrezOno_avg/avg_other_users)
