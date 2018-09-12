from flask import Flask, render_template, request, redirect
from flask import url_for, flash, jsonify
from flask import make_response

import os
import json
import requests
import string
import random
from functools import wraps

app = Flask(__name__)


@app.route('/')
@app.route('/main/')
def showMain():
    return render_template('first.html')


@app.route('/main.json/')
def showJson():
    with open(os.getcwd()+'/jsons/result_pic03.json') as data_file:
        data = json.load(data_file)
        return jsonify(data)


@app.route('/age.json/')
def showAgeJson():
    with open(os.getcwd()+'/jsons/result_pic03.json') as data_file:
        data = json.load(data_file)
        count = data['info']
        return jsonify(count)
        #for i in range(count):


@app.route('/size.json/')
def showWidthJson():
    with open(os.getcwd()+'/jsons/result_pic03.json') as data_file:
        data = json.load(data_file)
        return jsonify(data['info']['size'])


@app.route('/faceCountEx.json/')
def countFaceCountJson():
    with open(os.getcwd()+'/jsons/result_pic03.json') as data_file:
        data = json.load(data_file)
        count = data['info']['faceCount']
        """
        for i in range(count):
            print ("-----------------")
            return jsonify(data['faces'][i])
        """
        return jsonify(data['faces'])


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8888)
