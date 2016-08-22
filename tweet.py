import tweepy


ACCESS_TOKEN = '4715244873-AhymoSwvKoVsiVfvU62H9X7ehFYHGOmFqGipaOe'
ACCESS_TOKEN_SECRET = 'wbKYOVBnFF7Ul0FPnKxU3IgsdVOVO5OVqenJ3x1vUJYPw'
CONSUMER_TOKEN = 'a0rWLR8qWXO9pf4qY9OMxjgp1'
CONSUMER_SECRET = 'zyG5Of1v3ThuQ9ePf8qs4lirfVbTJhe3i6QmXDaagxmK2bjjNR'


auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


api = tweepy.API(auth)

# update status method
api.update_status('We ninjas tweet from the terminal!')
