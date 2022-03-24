from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import xml.etree.ElementTree as ET
from LogicLayer.orderBuilder import buildOrder
import sys

Tk().withdraw()
filename = askopenfilename(filetypes=[
    ('XML Files', '*.xml')
])


if(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        orders = buildOrder(root.iter('Employee'))

        print(orders)
                
    except:
        messagebox.showerror(title = 'Error', message='Some error occured, Please Try again.')
        sys.exit()
else:
    messagebox.showerror(title = 'Error', message = 'No file selected.')
    sys.exit()