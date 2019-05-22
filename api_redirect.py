import requests
from flask import Flask, request
app = Flask(__name__)
target = 'http://localhost:8088'

@app.route('/api', defaults={'path': ''})
@app.route('/api/<path:path>')
def catch_all(path):
    return requests.get('/'.join((target, path)), headers=request.headers).text


if __name__ == '__main__':
   app.run(port=8080)
