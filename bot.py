import requests
from tweepy import API
from tweepy import OAuthHandler
import keys as Keys

auth = OAuthHandler(Keys.consumer_key, Keys.consumer_secret)
auth.set_access_token(Keys.access_token, Keys.access_token_secret)
api = API(auth)

mentions = api.mentions_timeline(count=1)

for mention in mentions:
    print(mention.text)
    requests.post(Keys.host, json={
                  "id": "twitter@"+mention.user.id_str, "username": mention.user.screen_name, "campus": mention.text})
