import tweepy
import credentials

consumer_key = credentials.API_KEY
consumer_secret_key = credentials.API_SECRET_KEY
access_token = credentials.ACCESS_TOKEN
access_token_secret = credentials.ACCESS_TOKEN_SECRET

def tweet_update():

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)


    # mentions = api.mentions_timeline()
    #760840544117334016
    #760840544117334016
    # mentions['id'] = mentions.__dict__

    #tweet['id']
    # print(mentions)



    tweets = api.mentions_timeline()
    for t in tweets:

        # hashtags = [i['text'].lower() for i in t.__dict__['entities']['hashtags']]
        print("retweeted tweet of : "+t.in_reply_to_screen_name)
        # print("retweeted tweet of : "+t.__dict__['source'])


    # test_tweet = "Lol I made a bot"
    # for i in range(5):
    #     test_tweet = test_tweet + "lol"
    #     api.update_status(test_tweet)
    #     print("hi")


if __name__ == "__main__":
    tweet_update()

    # to run:   python .\SendTweets.py
