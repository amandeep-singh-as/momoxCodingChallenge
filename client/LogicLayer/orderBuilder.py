from tkinter import messagebox
import xml.etree.ElementTree as ET
import sys, json

from LogicLayer.service import fetchMenu


def buildOrder(empData):
    orders = []
    for emp in empData:
        order = {}
        customer = {}
        for child in emp:
            if(child.tag == 'Name'):
                customer['name'] = child.text
            elif(child.tag == 'Address'):
                customer['address'] = getAdress(child)
            elif(child.tag == 'Order'):
                items = getOrder(child.text.split(','))
        order['customer'] = customer
        order['items'] = items
        orders.append(order)
    return json.dumps(orders)
        
def getAdress(address):
    ad = {}
    for addr in address:
        if(addr.tag == 'Street'):
            ad['street'] = addr.text
        elif(addr.tag == 'City'):
            ad['city'] = addr.text
        elif(addr.tag == 'PostalCode'):
            ad['postal_code'] = addr.text
    return ad

def getOrder(order):
    menu =  fetchMenu()
    if(menu != "Error"):
        orders = []
        for o in order:
            temp = o.split('x ')
            orders.append({
                'id': list(filter(lambda item : item['name'] == temp[1], menu))[0]['id'],
                'amount': temp[0]
            })
        return orders
    else:
        messagebox.showerror(title = 'Error', message = 'Network error')
        sys.exit()