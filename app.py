from flask import Flask, render_template, request, jsonify
from grok import get_ad_copy
from tweets import create_tweet
from search import get_relevant_tweets
from images import generate_image_openai

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    
    product_event_info = request.form['product_event_info']
    city = request.form['city']
    
    # Generate ad copy, trend, and explanation
    ad_copies = get_ad_copy(product_event_info, city)
    
    # Return the result as a JSON object
    return jsonify(ad_copies)

@app.route('/publish', methods=['POST'])
def publish():
    tweet_text = request.json.get('tweet_text')
    image_url = request.json.get('image_url')
    
    # Post the tweet using Tweepy
    try:
        tweet_url = create_tweet(tweet_text, image_url)
        return jsonify({'status': 'success', 'message': 'Tweet posted successfully!', 'tweet_url': tweet_url})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/fetch_tweets', methods=['POST'])
def fetch_tweets():
    event_info = request.json.get('event_info')
    city = request.json.get('city')

    tweets = get_relevant_tweets(f"{event_info} in {city} -is:retweet", 3)

    return jsonify(tweets)


@app.route('/generate_image', methods=['POST'])
def generate_image():
    prompt = request.json.get('prompt')
    image = generate_image_openai(prompt)

    return jsonify({'image': image})

if __name__ == '__main__':
    app.run(debug=True)
