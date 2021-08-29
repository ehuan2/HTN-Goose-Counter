from flask import (
    Flask, request, Response,
    render_template,url_for 
)
from pathlib import Path
import http.client
import sys
from  os.path import join

app = Flask(__name__)
@app.route("/")
def landing_page():
    return render_template("index.html")

@app.route("/goose", methods = ["GET", "POST"])
def goose():
    if request.method == "POST":
        #Just an alternative way to fetch the details from html
        print("Goose Name: ",request.form["goose_name"])
        print("Goose Location: ",request.form["goose_loc"])
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
        return render_template("main.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)