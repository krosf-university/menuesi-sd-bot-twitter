import tweepy
import keys as Keys

auth = tweepy.OAuthHandler(Keys.consumer_key, Keys.consumer_secret)
auth.set_access_token(Keys.access_token, Keys.access_token_secret)
api = tweepy.API(auth)

# for follower in tweepy.Cursor(api.followers).items():
#     follower.follow()
#     print ("Followed everyone that is following " + user.name)