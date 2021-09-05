from flask import (
    Flask, request, Response
)
import http.client
import random
import redis_client
import util

app = Flask(__name__)

def getNickname():
    # first call the nickname generator to get a nickname
    conn = http.client.HTTPConnection("nickname-generator", 8081)
    conn.request("GET", "/")
    res = conn.getresponse()
    if res.status == 200:
        return util.unmarshalNickname(res.read())
    return None

def getCoordinates():
    return (random.randint(-100, 100), random.randint(-100, 100))

@app.route("/goose", methods = ["GET", "POST"])
def goose():
    if request.method == "POST":
        # (1) get the nickname from the nickname service
        nickname = getNickname()
        if nickname == None:
            # an error occurred, we just return an internal server error response
            return "internal server error", 500
        
        # (2) get random coordinates
        coordinates = getCoordinates()

        # (3) marshal to json
        gooseJson = util.marshalGoose(nickname, coordinates)

        # (3) save to redis
        redis_client.saveGoose(gooseJson)

        # (4) return response add in some good old headers
        return util.getResponse(gooseJson)

    elif request.method == "GET":
        geeseJson = redis_client.getGeese()
        return util.getResponse(geeseJson)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)