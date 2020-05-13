"""
 * Library name: Flask App
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

app = Flask(__name__)
filesLocation = "/tmp"


# Definition to create json output
def jsonOutputer(res):
    return jsonify(output=res)


# Definition to log requests
def errorLogging(logType, data):
    now = datetime.now().strftime(
        "%Y/%m/%d %H:%M:%S")
    app.logger.error(now + " (" + logType + ") " +
                     "[" + request.remote_addr + "] " + str(data))

# Login
@app.route('/user/login', methods=["POST"])
def userLogin():
    if request.headers.get("special_key") and request.form["user_name"] and request.form["user_password"]:
        # special token from android app
        token = request.headers.get("special_key")
        userName = request.form["user_name"]  # username sent via request
        password = request.form["user_password"]  # password sent via request
        return jsonOutputer("Parameters met")
    else:
        return jsonOutputer("Parameters not met")
