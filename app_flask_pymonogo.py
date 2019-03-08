#import os
from flask import Flask
from flask import request
#from pymongo import PyMongo
#import sys


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! \n"

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0", debug=True)
