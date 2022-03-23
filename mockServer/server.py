from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/api/v1/menu')
def fetchMenu():
    with open('./Data/menu.json', 'r') as menuFile:
        data = menuFile.read()
    
    menu = json.loads(data)
    return menu


@app.route('/api/v1/bulk/order', methods=['POST'])
def orderFood():
    data = request.get_json()

    return "order succesfull"
