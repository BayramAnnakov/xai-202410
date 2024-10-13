import dotenv

dotenv.load_dotenv()

import tweepy
import os

bearer_token = os.getenv("X_API_TOKEN")

# print(bearer_token)

client = tweepy.Client(bearer_token)


def get_relevant_tweets(query, max_results=10):
    print(query)
    response = client.search_recent_tweets(query, sort_order="relevancy", user_fields=["username"], expansions=["author_id"])
    
    print(response)


    includes = response.includes
    if "users" not in includes:
        return []
    users = includes["users"]
    users = {user["id"]: user for user in users}

    tweets = []


    for tweet in response.data:
        user_id = tweet["author_id"]
        user = users[user_id]
        url = f"https://twitter.com/{user['username']}/status/{tweet['id']}"

        tweets.append({
            "author_id": user_id,
            "text": tweet["text"],
            "id": tweet["id"],
            "url": url
        })

        if len(tweets) == max_results:
            break
        
    
    return tweets

# tweets = get_relevant_tweets("Fleet Week San Francisco", 3)

# print(tweets)



