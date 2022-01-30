from itertools import count
from os import access
from xml.etree.ElementInclude import include
import tweepy
import configparser
import pandas as pd

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

username = input("Enter username to search tweets..!")

tweets = tweepy.Cursor(
    api.user_timeline, exclude_replies=True, screen_name=username).items(150)

tweets_list = [[tweet.text, tweet.favorite_count] for tweet in tweets]

tweets_df = pd.DataFrame(tweets_list)
tweets_df.columns = ['Tweets', 'Likes']

datatoexcel = pd.ExcelWriter('tweets.xlsx')
tweets_df.to_excel(datatoexcel)
datatoexcel.save()

print("Successfully Done..!!")
