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
        { "price": 200, "date": "2015-01", "stocks": [100, 200, 100, 100, 100] },
        { "price": 300, "date": "2015-02", "stocks": [200, 300, 100, 100, 100] },
        { "price": 400, "date": "2015-03", "stocks": [300, 100, 100, 100, 100] },
        { "price": 300, "date": "2015-04", "stocks": [400, 200, 100, 100, 100] },
        { "price": 200, "date": "2015-05", "stocks": [500, 400, 100, 100, 100] },
        { "price": 200, "date": "2015-06", "stocks": [600, 300, 100, 100, 100] },
        { "price": 300, "date": "2015-07", "stocks": [500, 400, 100, 100, 100] },
        { "price": 400, "date": "2015-08", "stocks": [400, 200, 100, 100, 100] },
        { "price": 300, "date": "2015-09", "stocks": [100, 150, 100, 100, 100] },
        { "price": 200, "date": "2015-10", "stocks": [600, 150, 100, 100, 100] },
        { "price": 200, "date": "2015-11", "stocks": [700, 110, 100, 100, 100] },
        { "price": 300, "date": "2015-12", "stocks": [900, 230, 100, 100, 100] },
        { "price": 400, "date": "2016-01", "stocks": [300, 170, 100, 100, 100] },
        { "price": 300, "date": "2016-02", "stocks": [100, 180, 100, 100, 100] },
        { "price": 200, "date": "2016-03", "stocks": [300, 190, 100, 100, 100] },
        { "price": 200, "date": "2016-04", "stocks": [400, 170, 100, 100, 100] },
        { "price": 300, "date": "2016-05", "stocks": [200, 400, 100, 100, 100] },
        { "price": 400, "date": "2016-06", "stocks": [300, 600, 100, 100, 100] },
        { "price": 300, "date": "2016-07", "stocks": [500, 700, 100, 100, 100] },
        { "price": 200, "date": "2016-08", "stocks": [100, 100, 100, 100, 100] },
    ]
    }
    return jsonify(**county)

 
if __name__ == "__main__":
    app.run(host='localhost',port=5000,debug=True)