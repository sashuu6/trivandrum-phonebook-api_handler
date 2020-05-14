"""
 * Library name: App management API
 * File name : app.py
 * Author : Sashwat K
 * Last updated : 13 May 2020
"""

# Libraries for flask
from flask import Flask, jsonify, request
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
import os

from configparser import ConfigParser  # Library for importing .ini file

app = Flask(__name__)
filesLocation = "/tmp"

# Load database credentials via INI file
inilocation = "./parameters.ini"
iniFile = ConfigParser()
iniFile.read(inilocation)
hostName = iniFile[iniFile["deployment"]["model"]]["host_name"]
databaseName = iniFile[iniFile["deployment"]['model']]["database_name"]
databaseUsername = iniFile[iniFile["deployment"]['model']]["database_username"]
databasePassword = iniFile[iniFile["deployment"]['model']]["database_password"]


# Define log location
logLocation = "logs/log.txt"


# Definition to return json output
def jsonOutputer(code, res):
    return jsonify({"errorCode": code, "result": res})


# Definition to log requests
def theLogger(logType, data):
    now = datetime.now().strftime(
        "%Y/%m/%d %H:%M:%S")
    app.logger.error(now + " (" + logType + ") " +
                     "[" + request.remote_addr + "] " + str(data))

# Definition for handling user login
@app.route('/user/login', methods=["POST", "GET"])
def userLogin():
    if request.method == "POST" and request.headers.get("special_key") and request.form["user_name"] and request.form["user_password"]:
        # special token from android app
        token = request.headers.get("special_key")
        userName = request.form["user_name"]  # username sent via request
        password = request.form["user_password"]  # password sent via request
        theLogger("INFO", "Paramaters met")
        return jsonOutputer(200, "Parameters met")
    else:
        theLogger("ERROR", "Invalid method or missing headers")
        return jsonOutputer(404, "Parameters not met")


@app.errorhandler(404)
def invalid_route(e):
    theLogger("ERROR", "Invalid parameters, accessed invalid URL")
    return jsonOutputer(404, "Invalid parameters")


def main():
    handler = RotatingFileHandler(
        logLocation, maxBytes=10000, backupCount=1)
    handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)
    app.run(host="0.0.0.0")


if __name__ == "__main__":
    main()
