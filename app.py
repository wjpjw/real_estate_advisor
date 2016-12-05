from flask import Flask
from flask import jsonify
from flask import render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/date")   # price data of all counties for heatmap
def price_all_counties():
    prices={
        "items":[
            {"date": "2015-01", "all_prices": [
                {"county": 1000, "price":145},
                {"county": 1001, "price":232},
                {"county": 1003, "price":176},
                {"county": 1005, "price":351},
                {"county": 1007, "price":77},
                {"county": 1009, "price":761},
                {"county": 1011, "price":213},
                {"county": 1013, "price":144},
                {"county": 1015, "price":123},
                {"county": 1017, "price":321},
                {"county": 1019, "price":231},
                {"county": 1021, "price":321},
                {"county": 1023, "price":55},
                {"county": 1025, "price":731},
                {"county": 1027, "price":23},
                {"county": 1029, "price":344},
                {"county": 1031, "price":222}]
            },
            {"date": "2015-02", "all_prices": [
                {"county": 1000, "price":845},
                {"county": 1001, "price":532},
                {"county": 1003, "price":276},
                {"county": 1005, "price":51},
                {"county": 1007, "price":337},
                {"county": 1009, "price":61},
                {"county": 1011, "price":133},
                {"county": 1013, "price":44},
                {"county": 1015, "price":23},
                {"county": 1017, "price":231},
                {"county": 1019, "price":331},
                {"county": 1021, "price":213},
                {"county": 1023, "price":542},
                {"county": 1025, "price":31},
                {"county": 1027, "price":553},
                {"county": 1029, "price":44},
                {"county": 1031, "price":22}]
            },
            {"date": "2015-03", "all_prices": [
                {"county": 1000, "price":1145},
                {"county": 1001, "price":2232},
                {"county": 1003, "price":1736},
                {"county": 1005, "price":3514},
                {"county": 1007, "price":775},
                {"county": 1009, "price":7631},
                {"county": 1011, "price":2133},
                {"county": 1013, "price":1434},
                {"county": 1015, "price":1233},
                {"county": 1017, "price":3231},
                {"county": 1019, "price":2331},
                {"county": 1021, "price":3231},
                {"county": 1023, "price":553},
                {"county": 1025, "price":7331},
                {"county": 1027, "price":233},
                {"county": 1029, "price":3434},
                {"county": 1031, "price":2232}]
            },
            {"date": "2015-04", "all_prices": [
                {"county": 1000, "price":145},
                {"county": 1001, "price":232},
                {"county": 1003, "price":176},
                {"county": 1005, "price":351},
                {"county": 1007, "price":77},
                {"county": 1009, "price":761},
                {"county": 1011, "price":213},
                {"county": 1013, "price":144},
                {"county": 1015, "price":123},
                {"county": 1017, "price":321},
                {"county": 1019, "price":231},
                {"county": 1021, "price":321},
                {"county": 1023, "price":55},
                {"county": 1025, "price":731},
                {"county": 1027, "price":23},
                {"county": 1029, "price":344},
                {"county": 1031, "price":222}]
            },
            {"date": "2015-05", "all_prices": [
                {"county": 1000, "price":145},
                {"county": 1001, "price":232},
                {"county": 1003, "price":176},
                {"county": 1005, "price":351},
                {"county": 1007, "price":77},
                {"county": 1009, "price":761},
                {"county": 1011, "price":213},
                {"county": 1013, "price":144},
                {"county": 1015, "price":123},
                {"county": 1017, "price":321},
                {"county": 1019, "price":231},
                {"county": 1021, "price":321},
                {"county": 1023, "price":55},
                {"county": 1025, "price":731},
                {"county": 1027, "price":23},
                {"county": 1029, "price":344},
                {"county": 1031, "price":222}]
            },
            {"date": "2015-06", "all_prices": [
                {"county": 1000, "price":145},
                {"county": 1001, "price":232},
                {"county": 1003, "price":176},
                {"county": 1005, "price":351},
                {"county": 1007, "price":77},
                {"county": 1009, "price":761},
                {"county": 1011, "price":213},
                {"county": 1013, "price":144},
                {"county": 1015, "price":123},
                {"county": 1017, "price":321},
                {"county": 1019, "price":231},
                {"county": 1021, "price":321},
                {"county": 1023, "price":55},
                {"county": 1025, "price":731},
                {"county": 1027, "price":23},
                {"county": 1029, "price":344},
                {"county": 1031, "price":222}]
            },
            {"date": "2015-07", "all_prices": [
                {"county": 1000, "price":145},
                {"county": 1001, "price":232},
                {"county": 1003, "price":176},
                {"county": 1005, "price":351},
                {"county": 1007, "price":77},
                {"county": 1009, "price":761},
                {"county": 1011, "price":213},
                {"county": 1013, "price":144},
                {"county": 1015, "price":123},
                {"county": 1017, "price":321},
                {"county": 1019, "price":231},
                {"county": 1021, "price":321},
                {"county": 1023, "price":55},
                {"county": 1025, "price":731},
                {"county": 1027, "price":23},
                {"county": 1029, "price":344},
                {"county": 1031, "price":222}]
            },
            {"date": "2015-08", "all_prices": [
                {"county": 1000, "price":145},
                {"county": 1001, "price":232},
                {"county": 1003, "price":176},
                {"county": 1005, "price":351},
                {"county": 1007, "price":77},
                {"county": 1009, "price":761},
                {"county": 1011, "price":213},
                {"county": 1013, "price":144},
                {"county": 1015, "price":123},
                {"county": 1017, "price":321},
                {"county": 1019, "price":231},
                {"county": 1021, "price":321},
                {"county": 1023, "price":55},
                {"county": 1025, "price":731},
                {"county": 1027, "price":23},
                {"county": 1029, "price":344},
                {"county": 1031, "price":222}]
            },
            {"date": "2015-09", "all_prices": [
                {"county": 1000, "price":145},
                {"county": 1001, "price":232},
                {"county": 1003, "price":176},
                {"county": 1005, "price":351},
                {"county": 1007, "price":77},
                {"county": 1009, "price":761},
                {"county": 1011, "price":213},
                {"county": 1013, "price":144},
                {"county": 1015, "price":123},
                {"county": 1017, "price":321},
                {"county": 1019, "price":231},
                {"county": 1021, "price":321},
                {"county": 1023, "price":55},
                {"county": 1025, "price":731},
                {"county": 1027, "price":23},
                {"county": 1029, "price":344},
                {"county": 1031, "price":222}]
            },
            {"date": "2015-10", "all_prices": [
                {"county": 1000, "price":145},
                {"county": 1001, "price":232},
                {"county": 1003, "price":176},
                {"county": 1005, "price":351},
                {"county": 1007, "price":77},
                {"county": 1009, "price":761},
                {"county": 1011, "price":213},
                {"county": 1013, "price":144},
                {"county": 1015, "price":123},
                {"county": 1017, "price":321},
                {"county": 1019, "price":231},
                {"county": 1021, "price":321},
                {"county": 1023, "price":55},
                {"county": 1025, "price":731},
                {"county": 1027, "price":23},
                {"county": 1029, "price":344},
                {"county": 1031, "price":222}]
            },
            {"date": "2015-11", "all_prices": [
                {"county": 1000, "price":145},
                {"county": 1001, "price":232},
                {"county": 1003, "price":176},
                {"county": 1005, "price":351},
                {"county": 1007, "price":77},
                {"county": 1009, "price":761},
                {"county": 1011, "price":213},
                {"county": 1013, "price":144},
                {"county": 1015, "price":123},
                {"county": 1017, "price":321},
                {"county": 1019, "price":231},
                {"county": 1021, "price":321},
                {"county": 1023, "price":55},
                {"county": 1025, "price":731},
                {"county": 1027, "price":23},
                {"county": 1029, "price":344},
                {"county": 1031, "price":222}]
            },
            {"date": "2015-12", "all_prices": [
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100}]
            },
            {"date": "2016-01", "all_prices": [
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100}]
            },
            {"date": "2016-02", "all_prices": [
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100}]
            },
            {"date": "2016-03", "all_prices": [
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100}]
            },
            {"date": "2016-04", "all_prices": [
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100}]
            },
            {"date": "2016-05", "all_prices": [
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100}]
            },
            {"date": "2016-06", "all_prices": [
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100}]
            },
            {"date": "2016-07", "all_prices": [
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100}]
            },
            {"date": "2016-08", "all_prices": [
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100}]
            },
            {"date": "2016-09", "all_prices": [
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100},
                {"county": 001, "price":100}]
            },



        ]
    }
    return jsonify(**prices)

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