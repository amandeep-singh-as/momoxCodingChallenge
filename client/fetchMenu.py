import requests

def fetchMenu():
    url = "https://nourish.me/api/v1/menu"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    