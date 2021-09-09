# this module handles all the redis stuff
import redis
import util

# when we save the stuff to redis, 
def saveGoose(goose):
    r = redis.Redis(host="<db-container-name>", port=<port-number>, db=0)
    r.rpush("geese", goose)
    r.close()

def getGeese():
    r = redis.Redis(host="<db-container-name>", port=<port-number>, db=0)
    geese = []
    for bytes in r.lrange("geese", 0, -1):
        # unmarshal geese to remarshal with the counter
        geese.append(util.unmarshalGoose(bytes.decode()))
    counter = r.llen("geese")
    r.close()
    return util.marshalGeeseAndCounter(geese, counter) 
