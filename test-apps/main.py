"""
A simple app to show redis service integration.

Author: Ian Huston
License: See LICENSE.txt

"""
from flask import Flask, render_template, jsonify, abort
import os
import redis
import json

app = Flask(__name__)

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))


services = json.loads(os.getenv('VCAP_SERVICES'))
if 'redislabs' in services:
    redis_env = services['redislabs'][0]['credentials']
    provider = 'Redis Enterprise'
else:
    redis_env = services['p-redis'][0]['credentials']
    provider = 'Pivotal OSS Redis'



# r = redis.StrictRedis(host=redis_env['host'], port=int(redis_env['port']), password=redis_env['password'])
# r.info()


@app.route('/')
def keys():
    return render_template('index.html', provider=provider)

@app.route('/try')
def get_current_values():
    results = {}
    r = redis.StrictRedis(host=redis_env['host'], port=int(redis_env['port']), password=redis_env['password'])
    if r:
        (curtime, _) = r.time()
        r.lpush('scimmia', curtime)
        (last, second) = r.lrange('scimmia', 0, 1)
        results['delta'] = int(last) - int(second)
        return jsonify(results)
    else:
        return abort(500)


if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
