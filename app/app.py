import requests
import re
import os
import sqlite3
from services.Command import Command
from services.Command import CommandService
from services.Data import DataInitializer
from services.Data import DataController

from datetime import datetime, timedelta
from json import dumps, load, loads

from flask import Flask, render_template, Response, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """Return the index.html page"""
    return render_template('index.html')


@app.route('/command', methods=['GET'])
def getCommands():
    data = CommandService.getCommands()

    return Response(dumps(data), status=200, mimetype='application/json')


@app.route('/command', methods=['DELETE'])
def deleteCommands():
    DataController.deleteCommands()

    data = {"success": "true", "operation": "delete"}

    return Response(dumps(data), status=200, mimetype='application/json')


@app.route('/command', methods=['POST'])
def postCommand():
    print(request.json)
    CommandService.pushCommand(request.json['name'])

    data = {"Hi there": "This is a sample response"}
    return Response(dumps(data), status=200, mimetype='application/json')


@app.route('/api/<string:variable>', methods=['GET'])
def api_variable(variable):
    """This is an api endpoint with a string variable as url parameter"""
    data = {"You entered variable:": variable}
    return Response(dumps(data), status=200, mimetype='application/json')
    

if __name__ == '__main__':
    conn = sqlite3.connect('memory.db')
    DataInitializer.initialize()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    
    
