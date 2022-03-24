from email import message
from tkinter import messagebox
from urllib import response
import requests
import os
import json
from dotenv import load_dotenv
import ast

load_dotenv()

baseURL = os.getenv('BASE_URL')


def fetchMenu():
    try:
        response = requests.request("GET", 
        baseURL + '/menu', headers={}, data={})
    except:
        return "Error"
    
    if(response.status_code == 200):
        menu = json.loads(response.text)        
        return menu['dishes']
    else:
        return "Error"

fetchMenu()

def bulkOrder(orderData):
    try:
        response = requests.request("POST",
        baseURL + '/bulk/order', headers={}, 
        data=orderData)
    except:
        return "Error"

    if(response.status_code == 200):
        ordersFile = response.text
    else:
        return "Error" 