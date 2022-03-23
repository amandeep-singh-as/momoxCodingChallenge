from address import Address
from employee import Employee
from employeeEncoder import EmployeeEncoder
import json
from fileinput import filename
from re import T
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import xml.etree.ElementTree as ET


def genAddress(address):
    for elem in address:
        print(elem.tag, elem.text)
    

Tk().withdraw()
filename = askopenfilename(filetypes=[
    ('XML Files', '*.xml')
])



if(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    for employee in root.iter('Employee'):
        for child in employee:
            if(child.tag == 'Address'):
                print("***********************")
                genAddress(child)

    ad = Address("!2", "dakj", "dadfas")
    emp = Employee("mam", ad, "da", "adad", "ada")
    print(EmployeeEncoder().encode(emp))
    print(json.dumps(emp, cls=EmployeeEncoder))
else:
    messagebox.showerror(title='Alert', message="No file selected program will end now!!",)