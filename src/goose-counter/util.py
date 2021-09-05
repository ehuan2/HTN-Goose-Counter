# this module here will define some utility functions for http requests and json marshaling
from flask import Response
import json

# given the gooseJson, it'll add necessary headers for the response
def getResponse(goose):
    response = Response(goose)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Content-Type"] = "application/json"
    response.status = 200
    return response

# marshals the nickname and the location into json
def marshalGoose(nickname, coordinates):
    return json.dumps({
        "nickname": nickname["name"],
        "coordinates": {
            "x": coordinates[0],
            "y": coordinates[1]
        }
    })

def unmarshalGoose(goose):
    return json.loads(goose)

def unmarshalNickname(nickname):
    return json.loads(nickname)

def marshalGeeseAndCounter(geese, counter):
    return json.dumps({
        "geese": geese,
        "counter": counter
    })