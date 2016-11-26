from flask import Flask
from flask import jsonify
from flask import render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/county/<id>")
def countymap(id):
    county={
    "county": id+"wtf",  ## replace it with county name!
    "rate": 3,
    "stocks": ["s1", "s2", "s3", "s4", "s5"], 
    "history": [
        { "price": 200, "date": "2015-01", "stocks": [100, 100, 100, 100, 100] },
        { "price": 200, "date": "2015-02", "stocks": [100, 100, 100, 100, 100] },
        { "price": 200, "date": "2015-03", "stocks": [100, 100, 100, 100, 100] },
        { "price": 200, "date": "2015-04", "stocks": [100, 100, 100, 100, 100] },
        { "price": 200, "date": "2015-05", "stocks": [100, 100, 100, 100, 100] }
    ]
    }
    return jsonify(**county)

 
if __name__ == "__main__":
    app.run(host='localhost',port=5000,debug=True)