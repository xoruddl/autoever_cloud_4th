# redis 연결 실습

import redis

redis_pool = redis.ConnectionPool(host = "127.0.0.1", port = 6379,
                                  max_connections = 4)

with redis.StrictRedis(connection_pool = redis_pool) as con:

    con.delete("list")
    
    con.rpush("list", "adam")
    con.lpush("list", "rusia")
    con.rpush("list", "cidar")

    for imsi in con.lrange("list", 0, -1):
        print(imsi)
