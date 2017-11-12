#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pyttsx
import tweet_clean as tc
try:
    import json
except ImportError:
    import simplejson as json
import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
MAXTWEETS  = 10000000
curTweets = 0
stopStream = False
hindiTweetsFile = open('hindiTweets3.txt','a')



class MyStreamListner(tweepy.StreamListener):

	def __init__(self, api=None):
		super(MyStreamListner, self).__init__()
		self.num_tweets = 0

	def on_data(self, data):
		global curTweets
		global hindiTweetsFile
		global stopStream
		#try:
		#	with open('response.json', 'a') as f:
		#		f.write(data)
		#except BaseException as e:
		#	print str(e)
        
		
		dec = json.loads(data)

		
		if curTweets < MAXTWEETS:
			
			str1 = dec['text']
			str1.strip()
			str1 = tc.clean_tweet(str1)

			str_print = "["+"{0}".format(curTweets)+"]"+str1+"\n\n"
			print str_print

			str1 = str1+"\n"
			hindiTweetsFile.write(str1.encode('utf-8'))

			curTweets+=1

			return True

		else:
			stopStream = True
			return False

	def on_error(self, status):
		print status


if __name__ == '__main__':

	
	lis = MyStreamListner()
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	#api = tweepy.API(auth)

	wordFile = open('Most_Freq_Hindi_words_on_Twitter.txt','r')
	
	cord_UP = [77.09,23.87,84.67,30.41]
	cord_Ind = [68.1,6.46,97.39,35.5]

	strList = []

	for word in wordFile:
		word.strip()
		strList.append(word)

	wordFile.close()
	

	while stopStream is not True:
		try:
			stream = tweepy.Stream(auth, lis)
			stream.filter(track = [str.decode("utf-8") for str in strList])
		except:
			error_str = "Error Occured Restarting stream..."
			print "Error occured: ",sys.exc_info()[0]
			print "Restarting Stream........."
		

	
	hindiTweetsFile.close()
	print curTweets
