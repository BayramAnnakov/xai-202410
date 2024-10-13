import dotenv

dotenv.load_dotenv()

import os
import tweepy
from io import BytesIO
import requests

consumer_key = os.getenv("X_API_KEY")
consumer_secret = os.getenv("X_API_SECRET")

access_token = os.getenv("X_ACCESS_TOKEN")
access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)



def create_tweet(text, image_url=None):

    if image_url:
        image_response = requests.get(image_url)
        image = BytesIO(image_response.content)
        
        media = api.media_upload(filename="image.jpg", file=image)

        response = client.create_tweet(
            text=text,
            media_ids=[media.media_id]
        )
    else:
        response = client.create_tweet(
            text=text
        )
    return f"https://twitter.com/user/status/{response.data['id']}"