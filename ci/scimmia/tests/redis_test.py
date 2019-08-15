import nose
import redis
import os

def test_redis_timestamps():
    host = os.getenv('REDIS_HOST', "localhost")
    port = os.getenv('REDIS_PORT', 6379)
    redis_db = redis.StrictRedis(host=host, port=port, db=0)
    (last, second) = redis_db.lrange('scimmia', -2, 2)
    assert (last - second) < 180 # Less than 3 minutes between timestamps