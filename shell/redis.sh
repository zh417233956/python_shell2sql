#!/bin/bash
chcp 65001
redis-cli --raw -h 127.0.0.1 -p 6379 -n 1 SET User_list_1 "{\"UserId\": \"1\", \"UserName\": \"钟海\", \"orgid\": \"22\", \"flag\": \"1\", \"isjjr\": \"9\", \"RzRuzhiDate\": \"2019-07-11 14:55:01.690\", \"lasttime\": \"2019-07-11 14:55:01.690\", \"CompanyId\": \"1\"}"