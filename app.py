from flask import Flask, request, jsonify
from bson.json_util import dumps
from flask_pymongo import PyMongo


app = Flask(__name__)


dbName = "sample_restaurants"
dbPassword ="azertyuiop"
dbUri = "mongodb+srv://ghislain:{}@cluster0.lavoh.mongodb.net/{}?retryWrites=true&w=majority".format(dbPassword, dbName)
local = "mongodb://localhost:27017/company"
app.config["MONGO_URI"] = dbUri

mongo = PyMongo(app)

@app.route("/restaurants", methods=["GET"])
def restaurants():
    restau = mongo.db.restaurants.find()
    resp = dumps(restau)
    return resp

if __name__ == '__main__':
    app.run

        
