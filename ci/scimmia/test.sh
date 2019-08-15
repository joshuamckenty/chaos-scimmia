#!/bin/bash

# create a cluster (via service broker)
# create a DB against the cluster (via rladmin or CURL)
# set some keys
# in a loop, increment keys and save timestamps
# expose a REST API for current status of looping
# export TIMESTAMP=`redis-cli -h $REDIS_HOST --raw time | head -n 1`

redis-cli -h $REDIS_HOST lpush scimmia `redis-cli -h $REDIS_HOST --raw TIME | head -n 1`
nosetests -v -w /home/scimmia/tests

# LRANGE scimmia -2 2
# redis-cli -h $REDIS_HOST get foo
# echo "Done"
# exit 0