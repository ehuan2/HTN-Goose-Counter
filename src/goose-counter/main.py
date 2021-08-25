from flask import (
    Flask, request, Response
)
import http.client
import sys

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/goose", methods = ["GET", "POST"])
def goose():
    if request.method == "POST":
        conn = http.client.HTTPConnection("nickname-generator", 8081)
        conn.request("GET", "/")
        res = conn.getresponse()

        if res.status == 200:
            # add in some good old headers
            response = Response(res.read())
            response.headers["Access-Control-Allow-Origin"] = "*"
            response.headers["Content-Type"] = "application/json"
            response.status = 200
            return response

        return "internal server error", 500
    elif request.method == "GET":
        return "hello there"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)