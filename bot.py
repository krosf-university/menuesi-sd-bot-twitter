import requests
from tweepy import API
from tweepy import OAuthHandler
from time import sleep
import keys as Keys

auth = OAuthHandler(Keys.consumer_key, Keys.consumer_secret)
auth.set_access_token(Keys.access_token, Keys.access_token_secret)
api = API(auth)


def parser_mention(mention_text):
    return mention_text.split()[1]


def last_id():
    f_read = open('lastmention.txt', 'r')
    last_id = int(f_read.read().strip())
    f_read.close()
    return last_id


def store_id(last_id):
    f_write = open('lastmention.txt', 'w')
    f_write.write(str(last_id))
    f_write.close()


def suscribe():

    mentions = api.mentions_timeline(last_id())

    for mention in mentions:
        sleep(5)
        store_id(mention.id)
        print(mention.text)
        print(parser_mention(mention.text))
        requests.post(Keys.host, json={
            "id": "twitter@"+mention.user.id_str, "username": mention.user.screen_name, "campus": parser_mention(mention.text)})


while(True):
    suscribe()
    sleep(5)
