#!/bin/bash
exe_secelt(){
REDIS_KEY=$1
REDIS_VALUE=$2
REDIS_VALUE=${REDIS_VALUE//\\\"/\"}
REDIS_VALUE=${REDIS_VALUE//\\T/T}
echo $REDIS_VALUE
redis-cli --raw -h 127.0.0.1 -p 6379 -n 1 SET $REDIS_KEY $REDIS_VALUE
}
exe_secelt $1 $2