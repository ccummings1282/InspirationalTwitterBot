import tweepy
from os import environ
import random
import heroku
from time import sleep

# Set twitter credentials, these are stored in Heroku Config Vars
consumer_key = environ['API_KEY']
consumer_secret_key = environ['API_SECRET_KEY']
access_token = environ['ACCESS_TOKEN']
access_token_secret = environ['ACCESS_TOKEN_SECRET']

def tweet_update():

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # List of formatted inspirational quotes.
    quotes = ["\"Believe you can and you're halfway there.\" \n-Theodore Roosevelt",
    "\"When you have a dream, you've got to grab it and never let go.\" \n-Carol Burnett",
    "\"I can't change the direction of the wind, but I can adjust my sails to always reach my destination.\" \n-Jimmy Dean",
    "\"No matter what you're going through, there's a light at the end of the tunnel.\" \n-Demi Lovato",
    "\"It is our attitude at the beginning of a difficult task which, more than anything else, will affect its successful outcome.\" \n-William James",
    "\"Life is like riding a bicycle. To keep your balance, you must keep moving.\" \n-Albert Einstein"]
    # "\"text\" \n-author",



    # Sends a reply to the most recent tweet which contains: #NeedInspiration
    for tweet in tweepy.Cursor(api.search, q=('#NeedInspiration -filter:retweets'), lang='en').items(1):
        try:
            handle = tweet.user.screen_name # author's twitter handle from selected tweet
            text = tweet.text # text from selected tweet
            random_quote = random.choice(quotes) # random quote from list of quotes

            # compose response to send to selected tweet
            response = ("Hey @" + handle + ", here's an inspiring quote:\n" + random_quote)
            
            # likes, then sends reponse to the selected tweet
            tweet.favorite()
            tweet = api.update_status(response, tweet.id)

            # prints success log to console
            print('Success! Replied to @' + handle + '\'s tweet:\n\n' + text + '\n')

            # sleep for 15 minutes
            # sleep(900)
        
        except tweepy.TweepError as e:
            print(e.reason) # Prints the reason for error if thrown.

        except StopIteration:
            break


if __name__ == "__main__":
    tweet_update()

    # Run with terminal:   python .\SendTweets.py
