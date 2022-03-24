from tkinter import messagebox
import xml.etree.ElementTree as ET
import sys

from LogicLayer.service import fetchMenu


def buildOrder(empData):
    orders = []

    for emp in empData:
        order = {}
        for child in emp:
            if(child.tag == 'Address'):
                order[child.tag] = getAdress(child)
            elif(child.tag == 'Order'):
                order['items'] = getOrder(child.text.split(','))
            else:
                order[child.tag] = child.text
        orders.append(order)
    return orders
        
def getAdress(address):
    ad = {}
    for addr in address:
        ad[addr.tag] = addr.text
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