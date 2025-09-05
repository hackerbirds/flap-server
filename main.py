import time

import redis
import base64
from quart import Quart, request

app = Quart(__name__)
db = redis.Redis(host='redis', port=6379)

@app.route('/')
async def index():
    return f'Hello World!'

@app.post('/preparePackage')
async def preparePackage():
    data = await request.get_json()
    packageId = data['id']
    packageData = data['encryptedData']
    db.set(packageId, packageData)
    return {"status": 200}

@app.get('/package')
async def receivePackage():
    data = request.args
    pkgId = data.get('id')
    pkgData = db.get(pkgId)

    if pkgData is None:
        return {"status": 404}

    return {"status": 200, "encryptedData": pkgData.decode("ascii")}
