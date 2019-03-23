import requests
from bottle import run, post, request, response
from keys import credentials_twitter  # localfile
from json import dumps

def image_twitter(url, campus):
    requestz = requests.get(url, stream=True)
    if requestz.status_code == 200:
        filename = "file.jpg"
        with open(filename, 'wb') as image:
            for chunk in requestz:
                image.write(chunk)
        credentials_twitter().update_with_media(filename, status=campus)


@post('/')
def index():
    json = request.json
    print(json)
    image_twitter(json['image'], json['campus'])
    response.content_type = "application/json"
    return dumps({"correcto":"true"})


run(host="localhost", port=4000)
