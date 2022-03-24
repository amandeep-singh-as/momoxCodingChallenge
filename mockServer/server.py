from flask import Flask, request
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/api/v1/menu')
def fetchMenu():
    with open('./Data/menu.json', 'r') as menuFile:
        data = menuFile.read()
    menu = json.loads(data)
    return menu


@app.route('/api/v1/bulk/order', methods=['POST'])
def orderFood():
    data = request.data
    resultFileName = './Data/results/' + datetime.now().strftime("Result_%d-%m-%Y%H-%M-%S")
    with open(resultFileName, 'wb') as resultFile:
        resultFile.write(data)
    return resultFileName
