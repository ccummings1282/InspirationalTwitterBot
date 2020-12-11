import tweepy
import credentials
from time import sleep

# Set twitter credentials
consumer_key = credentials.API_KEY
consumer_secret_key = credentials.API_SECRET_KEY
access_token = credentials.ACCESS_TOKEN
access_token_secret = credentials.ACCESS_TOKEN_SECRET

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



    # Sends a reply to the most recent tweet which contains: #wantinspiration
    for tweet in tweepy.Cursor(api.search, q=('#hi -filter:retweets'), lang='en').items(1):
        try:
            name = tweet.user.screen_name
            text = tweet.text
            reply = ("Hey @" + name + ", here's a cool quote:\n" + quotes[0])
            
            tweet = api.update_status(reply, tweet.id)
            print('Replied to @' + name + '\'s tweet, which was:\n\n' + text + '\n\n')

            sleep(1)
        
        except tweepy.TweepError as e:
            # Prints the reason for error if thrown.
            print(e.reason)

        except StopIteration:
            break


if __name__ == "__main__":
    tweet_update()

    # Run with terminal:   python .\SendTweets.py
