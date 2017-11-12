# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:14:09 2017

@author: HP
"""
import re
import hindi_stemmer as hs
import string
from collections import defaultdict

exclude1 = set([u'।',u'-',u',',u'ॽ',u'॥',u'(',u')',u'.',u'…', u'…', u'०', u'१', u'२', u'३', u'४', u'५', u'६', u'७', u'८', u'९'])
exclude2 = set(string.punctuation)
stopwords=[]
hindi_stop_words = open('hindi_stopwords.txt','r')
for line in hindi_stop_words:
        stopwords.append(line.decode('utf-8').strip('\n'))
        
stopwords = set(stopwords)

emoji_pattern = re.compile(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)


def clean_tweet(tweet):
    
    tweet_new = Remove_AlphaNumeric(tweet)
   
    
    
    tweet_new = Remove_Punctuation(tweet_new)

    tweet_new = Remove_stopwords(tweet_new)
    
    tweet_new = Remove_stem(tweet_new)

    tweet_new = Remove_Emoji(tweet_new)
 
    return tweet_new


def Remove_AlphaNumeric(tweet):

    tweet_new = re.sub("[a-zA-Z0-9@]","",tweet)
    tweet_new = re.sub("[\nEOF]"," ",tweet_new)
    
    return tweet_new

def Remove_Emoji(data):
    

    if not data:
        return data
    if not isinstance(data, basestring):
        return data
    try:
        # UCS-4
        patt = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
    except re.error:
        # UCS-2
        patt = re.compile(u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')
    return patt.sub('', data)
    #remove_emoji(tweet)


def Remove_Punctuation(tweet):
     ### Removing punctuations
    tweet_new = ''.join(ch for ch in tweet if ch not in exclude1)
    tweet_new = ''.join(ch for ch in tweet_new if ch not in exclude2)
    return tweet_new
    
def Remove_stopwords(tweet):
    tweet_new = " ".join([i for i in tweet.split() if i not in stopwords])
    return tweet_new

def Remove_stem(tweet):
    tweet_list = tweet.split()
    tweet_list = [hs.hi_stem(word) for word in tweet_list]
    tweet_new = " ".join(tweet_list)
    return tweet_new    

def clean_tweet_by_frequency(tweet_file_name, processed_tweets_file_name):
    
    frequency = defaultdict(int)
    tweet_file = open(tweet_file_name,'r')
    new_tweet_file = open(processed_tweets_file_name,'w')
    
    for tweet in tweet_file:
        for token in tweet.split():
            frequency[token] += 1
    
    tweet_file.seek(0)
    
    
    for tweet in tweet_file:
        text = [token for token in tweet.split() if frequency[token]>1]
        if text is not None:
            new_tweet_file.write(" ".join(text)+"\n")
        
        
    tweet_file.close()
    new_tweet_file.close()    


#for ch in str:
#    print ch
