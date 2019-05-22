import requests
from flask import Flask, request
app = Flask(__name__)
target = 'http://localhost:8088'

@app.route('/jabber', defaults={'path': ''})
@app.route('/jabber/<path:path>')
def catch_all(path):
    return requests.get('/'.join((target, path)), headers=request.headers).text


if __name__ == '__main__':
   app.run(port=8021)
