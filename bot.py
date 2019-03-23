import requests
import socketserver
import http.server
from time import localtime, strftime
from time import sleep
from keys import credentials_twitter  # localfile
from pprint import pprint


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


def media_url(mention):
    return mention.extended_entities['media'][0]['media_url']


def get_username(mention):
    return '@' + mention.user.screen_name


def image():
    mentions = credentials_twitter().mentions_timeline(last_id())
    for mention in mentions:
        sleep(5)
        store_id(mention.id)
        print(parser_mention(mention.text))
        if hasattr(mention, "extended_entities"):
            requests.post("http://localhost:8081/image",
                          json={"id": "twitter@"+mention.user.id_str, "url": media_url(mention), "campus": parser_mention(mention.text.lower()), "date": strftime("%d%m%Y", localtime())})
        else:
            credentials_twitter().update_status(get_username(mention) +
                                                "Enga crack, dame una foto.", mention.id)


# mentions = credentials_twitter().mentions_timeline(count=1)
# for mention in mentions:
#     pprint(hasattr(mention, "extended_entities"))

while(True):
    image()
    sleep(30)
