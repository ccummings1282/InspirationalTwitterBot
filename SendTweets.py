import json
import tweepy
import random
from os import environ

# Set twitter credentials, these are stored in AWS Lambda Config Vars
def lambda_handler(event, context):
    tweet_update()


def tweet_update():

    print('getting credentials')
    consumer_key = environ['API_KEY']
    consumer_secret_key = environ['API_SECRET_KEY']
    access_token = environ['ACCESS_TOKEN']
    access_token_secret = environ['ACCESS_TOKEN_SECRET']

    print('authenticating')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)


    # List of formatted inspirational quotes.
    quotes = ["\"Believe you can and you're halfway there.\" \n-Theodore Roosevelt",
    "\"When you have a dream, you've got to grab it and never let go.\" \n-Carol Burnett",
    "\"I can't change the direction of the wind, but I can adjust my sails to always reach my destination.\" \n-Jimmy Dean",
    "\"No matter what you're going through, there's a light at the end of the tunnel.\" \n-Demi Lovato",
    "\"It is our attitude at the beginning of a difficult task which, more than anything else, will affect its successful outcome.\" \n-William James",
    "\"Life is like riding a bicycle. To keep your balance, you must keep moving.\" \n-Albert Einstein",
    "\"Act as if what you do makes a difference. It does.\" \n-William James",
    "\"Success is not final, failure is not fatal: it is the courage to continue that counts.\" \n-Winston Churchill",
    "\"Never bend your head. Always hold it high. Look the world straight in the eye.\" \n-Helen Keller",
    "\"What you get by achieving your goals is not as important as what you become by achieving your goals.\" \n-Zig Ziglar",
    "\"Just don't give up trying to do what you really want to do. Where there is love and inspiration, I don't think you can go wrong.\" \n-Ella Fitzgerald",
    "\"Limit your 'always' and your 'nevers.'\" \n-Amy Poehler",
    "\"You are never too old to set another goal or to dream a new dream.\" \n-C.S. Lewis",
    "\"Try to be a rainbow in someone else's cloud.\" \n-Maya Angelou",
    "\"You do not find the happy life. You make it.\" \n-Camilla Eyring Kimball",
    "\"Inspiration comes from within yourself. One has to be positive. When you're positive, good things happen.\" \n-Deep Roy",
    "\"Sometimes you will never know the value of a moment, until it becomes a memory.\" \n-Dr. Seuss",
    "\"The most wasted of days is one without laughter.\" \n-E. E. Cummings",
    "\"You must do the things you think you cannot do.\" \n-Eleanor Roosevelt",
    "\"It isn't where you came from. It's where you're going that counts.\" \n-Ella Fitzgerald",
    "\"It is never too late to be what you might have been.\" \n-George Eliot",
    "\"Stay close to anything that makes you glad you are alive.\" \n-Hafez",
    "\"Happiness often sneaks in through a door you didn't know you left open.\" \n-John Barrymore",
    "\"We must be willing to let go of the life we planned so as to have the life that is waiting for us.\" \n-Joseph Campbell",
    "\"Life changes very quickly, in a very positive way, if you let it.\" \n-Lindsey Vonn",
    "\"Never limit yourself because of others’ limited imagination; never limit others because of your own limited imagination.\" \n-Mae Jemison",
    "\"Let us make our future now, and let us make our dreams tomorrow's reality.\" \n-Malala Yousafzai",
    "\"If I cannot do great things, I can do small things in a great way.\" \n-Martin Luther King Jr.",
    "\"The bad news is time flies. The good news is you're the pilot.\" \n-Michael Altshuler",
    "\"Don't wait. The time will never be just right.\" \n-Napoleon Hill",
    "\"A champion is defined not by their wins but by how they can recover when they fall.\" \n-Serena Williams",]


    # Sends a reply to the most recent tweet which contains: #NeedInspiration
    for tweet in tweepy.Cursor(api.search, q=('#NeedInspiration -filter:retweets'), lang='en').items(3):
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

        
        except tweepy.TweepError as e:
            print(e.reason) # Prints the reason for error if thrown.

        except StopIteration:
            break
