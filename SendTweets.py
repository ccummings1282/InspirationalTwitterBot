import tweepy
import credentials
from time import sleep

consumer_key = credentials.API_KEY
consumer_secret_key = credentials.API_SECRET_KEY
access_token = credentials.ACCESS_TOKEN
access_token_secret = credentials.ACCESS_TOKEN_SECRET

def tweet_update():

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)


    # Sends a reply to two tweets which contain #hello
    for tweet in tweepy.Cursor(api.search, q=('#hello -filter:retweets'), lang='en').items(2):
        try:
            name = tweet.user.screen_name
            text = tweet.text
            reply = "@%s Hey!" % (name)
            
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
