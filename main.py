import time

import redis
from quart import Quart

app = Quart(__name__)
db = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    return f'Hello World'