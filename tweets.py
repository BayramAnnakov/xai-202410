import dotenv

dotenv.load_dotenv()

import os
import tweepy

consumer_key = os.getenv("X_API_KEY")
consumer_secret = os.getenv("X_API_SECRET")

access_token = os.getenv("X_ACCESS_TOKEN")
access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)


def create_tweet(text):
    response = client.create_tweet(
        text=text
    )
    return f"https://twitter.com/user/status/{response.data['id']}"