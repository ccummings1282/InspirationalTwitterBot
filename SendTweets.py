import tweepy
import credentials

consumer_key = credentials.API_KEY
consumer_secret_key = credentials.API_SECRET_KEY
access_token = credentials.ACCESS_TOKEN
access_token_secret = credentials.ACCESS_TOKEN_SECRET

# consumer_key = "49RYz6lxn94GlZx6BOVmafFCV"
# consumer_secret_key = "CywArKb9kyFYk2lsVnsIlxDsM9RBrIpO89SUDGh6PQGJbdqlxF"
# access_token = "3893377102-MvBTAExOJR698ggpJDI0zUuWDZHsmHSxauOqfP2"
# access_token_secret = "i8sHdoncY7bIXX4zmRDzEieCnVWefKkgFnqClm54sfXXS"

def tweet_update():

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    test_tweet = "Lol I made a bot"
    for i in range(50):
        test_tweet = test_tweet + "lol"
        api.update_status(test_tweet)
        print("hi")


if __name__ == "__main__":
    tweet_update()
