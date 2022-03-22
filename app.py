from address import Address
from employee import Employee
from employeeEncoder import EmployeeEncoder
import json
from fileinput import filename
from re import T
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import xml.etree.ElementTree as ET



def genAddress(address):
    for elem in address:
        print(elem.tag, elem.text)
    

Tk().withdraw()
filename = askopenfilename()
print(filename)

tree = ET.parse(filename)
root = tree.getroot()

print(root.tag)

for employee in root.iter('Employee'):
    for child in employee:
        if(child.tag == 'Address'):
            print("***********************")
            genAddress(child)

ad = Address("!2", "dakj", "dadfas")
emp = Employee("mam", ad, "da", "adad", "ada")
print(EmployeeEncoder().encode(emp))
print(json.dumps(emp, cls=EmployeeEncoder))