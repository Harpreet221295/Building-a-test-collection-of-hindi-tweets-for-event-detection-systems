#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import the necessary package to process data in JSON format
import io
import tweet_clean as tc
import codecs
try:
    import json
except ImportError:
    import simplejson as json

encoding = 'utf-8'
# We use the file saved from last step as example
#tweets_filename = 'F:\MainDesktop\Text mining\response.json'
#tweets_filename2 = 'F:\MainDesktop\Text mining\response_Decoded.txt'
#tweets_file = codecs.open(r'F:\MainDesktop\Text mining\response.json', 'r', encoding = "utf-8")
tweets_file = open(r'F:\MainDesktop\Text mining\response.json', 'r')
#tweets_file = open(r'F:\MainDesktop\Text mining\response.json','r')
#tweets_file2 = codecs.open(r'F:\MainDesktop\Text mining\response_Decoded.txt','w',encoding = "utf-8")
tweets_file2 = open(r'F:\MainDesktop\Text mining\response_Decoded2.txt', 'w')

count=0

tweet_dataset=[]

for line in tweets_file:
    
    count+=1
    
    if count > 5:
        break
    
    
    try:
        # Read in one line of the file, convert it into a json object 
        tweet = json.loads(line.strip())
        if 'text' in tweet: # only messages contains 'text' field is a tweet
#            print "\n\n\n"
#            print tweet['id'] # This is the tweet's id
#            tweets_file2.write(unicode(str(tweet['id'])+'\n','utf-8'))
#            
#            print tweet['created_at'] # when the tweet posted
#            tweets_file2.write(unicode(str(tweet['created_at'])+'\n','utf-8'))
            
            

            print tc.clean_tweet(tweet['text'])
            #tweet_dataset.append(tweet['text'].encode('utf-8')) # content of the tweet
            #tweets_file2.write((tweet['text']+'\n').encode('utf-8'))

#            print tweet['user']['id'] # id of the user who posted the tweet
#            tweets_file2.write(unicode(str(tweet['user']['id'])+'\n','untf-8'))
#            
#            print tweet['user']['name'] # name of the user, e.g. "Wei Xu"
#            tweets_file2.write(unicode(str(tweet['user']['name'])+'\n','utf-8'))
#            
#            print tweet['user']['screen_name'] # name of the user account, e.g. "cocoweixu"
#            tweets_file2.write(unicode(str(tweet['user']['screen_name'])+'\n','utf=8'))

#            hashtags = []
#            for hashtag in tweet['entities']['hashtags']:
#            	hashtags.append(hashtag['text'])
#            
#            print hashtags
#            tweets_file2.write(unicode(str(hashtags)+'\n','utf-8'))
#
#            tweets_file2.write("\n\n\n")
    except:
        # read in a line is not in JSON format (sometimes error occured)
        continue
    
    


tweets_file.close()
tweets_file2.close()

#tweet_corp = [twt.split() for twt in tweet_dataset]
#
#for twt in tweet_corp:
#    for word in twt:
#        print word.decode('utf-8')
        
        
