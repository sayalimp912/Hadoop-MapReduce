#!/usr/bin/env python
from __future__ import division
import sys
import string
results={}

for line in sys.stdin:
  (tweet_hour,good_bad) = line.strip().split('\t')

  if tweet_hour in results:
    results[tweet_hour].append(good_bad)

  else:
    results[tweet_hour]=[]
    results[tweet_hour].append(good_bad)

total_word_sum=0
total_badword_sum=0
    
for added_list in results.keys():
  word=results[added_list]
  if len(word)>1:
    for x in range(len(word)):
      total_word_sum=total_word_sum+int(word[x].split('_')[0])
      total_badword_sum=total_badword_sum+int(word[x].split('_')[1])
  ratio=total_badword_sum/total_word_sum
  print '%s\t%s'% (added_list,ratio)
