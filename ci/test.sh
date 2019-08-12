#!/bin/bash

# create a cluster (via service broker)
# create a DB against the cluster (via rladmin or CURL)
# set some keys
# in a loop, increment keys and save timestamps
# expose a REST API for current status of looping
TIMESTAMP = `redis-cli --raw time | head -n 1`
redis-cli -h $REDIS_HOST lpush scimmia $TIMESTAMP
# LRANGE scimmia -2 2
# redis-cli -h $REDIS_HOST get foo
echo "Done"
exit 0