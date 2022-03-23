from Models.Address import Address
from Models.Employee import Employee
from Encoder.EmployeeEncoder import EmployeeEncoder
import json
from fileinput import filename
from re import T
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import xml.etree.ElementTree as ET
import requests
import os, sys
from dotenv import load_dotenv

load_dotenv()

baseURL = os.getenv('BASE_URL')

payload={}
headers = {}

try:
    response = requests.request("GET", baseURL+'/menu', headers=headers, data=payload)
except:
    messagebox.showerror(title='Alert', message='Some network error!!')
    sys.exit()

if(response.status_code == 200):
    menu = response.text
else:
    messagebox.showerror(title='Alert', message='Error in fetching Menu')
    sys.exit()



# Tk().withdraw()
# filename = askopenfilename(filetypes=[
#     ('XML Files', '*.xml')
# ])



# if(filename):
#     tree = ET.parse(filename)
#     root = tree.getroot()

#     for employee in root.iter('Employee'):
#         for child in employee:
#             if(child.tag == 'Address'):
#                 print("***********************")
#                 genAddress(child)

   
# else:
#     messagebox.showerror(title='Alert', message="No file selected program will end now!!",)