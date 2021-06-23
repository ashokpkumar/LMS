
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import time
import datetime
import json
#from sqlalchemy.ext.serializer import loads, dumps

from flask import request, render_template
import os


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug = True)