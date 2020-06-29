#!/usr/bin/python3.8

import tweepy
import logging
from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def main():
    api = create_api()
    for status in tweepy.Cursor(api.user_timeline, id='RyanJosephDev').items():
        print("status {} \n", status.text)
        

if __name__ == "__main__":
    main()
    
    
    