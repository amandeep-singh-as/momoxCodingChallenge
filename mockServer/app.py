from crypt import methods
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/api/fetchMenu')
def fetchMenu():
    with open('./Data/menu.json', 'r') as menuFile:
        data = menuFile.read()
    
    menu = json.loads(data)
    return menu


@app.route('/api/orderFood', methods=['POST'])
def orderFood():
    data = request.get_json()

    return "order succesfull"
