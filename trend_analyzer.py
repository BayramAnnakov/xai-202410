import dotenv

dotenv.load_dotenv()

import tweepy
import os

bearer_token = os.getenv("X_API_TOKEN")

# print(bearer_token)

client = tweepy.Client(bearer_token)

#response = client.search_recent_tweets("San Francisco", max_results=10)
users = client.get_users(usernames=["jack", "elonmusk"])

print(users)

response = client.get_users_tweets(id=44196397, max_results=10)

print(response.meta)
tweets = response.data


for tweet in tweets:
    print(tweet.id)
    print(tweet.text)


