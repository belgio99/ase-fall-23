from flask import Flask, render_template, request, make_response, jsonify
import requests

app = Flask(__name__, instance_relative_config=True)

data_list = []

@app.route('/addLog',methods = ['POST'])
def addLog():
    data_list.append(request.data)
    print(data_list)

@app.route('/getLog',methods = ['GET'])
def getLog():
    print(data_list)
