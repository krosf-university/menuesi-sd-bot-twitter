import requests
from bottle import run, post, request
from keys import credentials_twitter  # localfile


def image_twitter(url, campus):
    requestz = requests.get(url, stream=True)
    if requestz.status_code == 200:
        filename = url[url.rfind("/")+1:]
        with open(filename) as image:
            for chunk in requestz:
                image.write(chunk)
        credentials_twitter().update_with_media(filename, status=campus)


@post('/')
def index():
    json = request.json
    image_twitter(json['url'], json['campus'])
    return "Es Correcto"


run(host="localhost", port=8080)
