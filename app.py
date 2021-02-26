from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
from sqlalchemy import create_engine
import sqlalchemy
import os

#################################################
# Database Setup
#################################################
query = "wine.sql"

rds_connection_string = f"postgres://pyuepqwjtgkmfx:75425df2df071f0b81f4e7bca3ad4f7e5cbefb361b0c30331d30196e3b8ef83a@ec2-34-198-31-223.compute-1.amazonaws.com:5432/da75s215ag1n2i"
engine = create_engine(f'postgres://pyuepqwjtgkmfx:75425df2df071f0b81f4e7bca3ad4f7e5cbefb361b0c30331d30196e3b8ef83a@ec2-34-198-31-223.compute-1.amazonaws.com:5432/da75s215ag1n2i')

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')

@app.route("/wines")
def wines():
    result = []
    count = 0
    result_set = engine.execute("select * from redwine UNION select * from whitewine")
    for row in result_set:
        data = {}
        count += 1
        data["Record"] = count 
        data["Type"] = row.type
        data["Fixed Acidity"] = row.fixed_acidity
        data["Volatile Acidity"] = row.volatile_acidity
        data["Citric Acid"] = row.citric_acid
        data["Residual Sugar"] = row.residual_sugar
        data["Chlorides"] = row.chlorides
        data["Free Sulfur Dioxide"] = row.free_sulfur_dioxide
        data["Total Sulfur Dioxide"] = row.total_sulfur_dioxide
        data["Density"] = row.density
        data["pH"] = row.pH
        data["Sulphates"] = row.sulphates
        data["Alcohol"] = row.alcohol
        data["Quality"] = row.quality

        result.append(data)

    return jsonify(result)
    
if __name__ == "__main__":
    app.run(debug=True)