#!/usr/bin/env python
from __future__ import division
import sys
import string

tweet_count = 0
day = None
count=0
avg={}

for line in sys.stdin:
  (key,val) = line.strip().split('\t')
  
  if day != key:
    if day:
      average_day=tweet_count/52
      avg[average_day]=day
      tweet_count = 0
    day = key
  try:
    tweet_count = tweet_count + int(val)
  except:
    continue
average_day=tweet_count/52
avg[average_day]=day

print avg
print avg[max(avg.keys(),key=float)]

