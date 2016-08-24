import tweepy


auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


api = tweepy.API(auth)

# update status method
api.update_status('We ninjas tweet from the terminal!')
