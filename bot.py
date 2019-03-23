import requests
import socketserver
import http.server
from time import localtime, strftime
from time import sleep
from keys import credentials_twitter  # localfile


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


def image():
    mentions = credentials_twitter().mentions_timeline(last_id())
    for mention in mentions:
        sleep(5)
        store_id(mention.id)
        print(parser_mention(mention.text))
        requests.post("http://macos.local:8081/image", json={
            "id": "twitter@"+mention.user.id_str, "url": mention.media.media_url_https, "campus": parser_mention(mention.text), "date": strftime("%d%m%Y", localtime())})


while(True):
    image()
    sleep(5)
