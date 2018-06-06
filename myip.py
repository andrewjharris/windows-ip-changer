import tkinter as tk
import os
import sys
from tkinter import *
window = tk.Tk()
window.title("Arlen's IP adjuster")
window.geometry("400x170")
#-- global variables
myip = ('192.168.0.100')
mysub = ('255.255.255.0')
mygate = ('192.168.0.1')
def chunk():
    os.system('cls')

def staticip():
	global myip
	global mysub
	global mygate
	myip = str(entry_field1.get()).lower()
	mysub = str(entry_field2.get()).lower()
	mygate = str(entry_field3.get()).lower()
	set_static = ('netsh int ip set address "local area connection" static ' + str(myip) + " " + str(mysub) + " " + str(mygate) + ' 1')
	os.system(str(set_static))
def dynamicip():
	os.system('netsh int ip set address "local area connection" dhcp')
	
# Static Button
button1 = tk.Button(text="Static IP", command=staticip, bg="red", fg="white", width=18)
button1.grid(column=0, row=3, sticky="W")

# Dynamic BUTTON
button2 = tk.Button(text="Dynamic IP", command=dynamicip, bg="yellow", fg="black", width=18)
button2.grid(column=1, row=3, sticky="W")

# Label MyIP
label1 = tk.Label(text="IP Address")
label1.grid(column=0, row=0, sticky="W")

# Entry MyIP
entry_field1 = tk.Entry()
entry_field1.grid(column=1, row=0, sticky="W")
entry_field1.insert(tk.END, '192.168.0.100')

# Label Subnet
label2 = tk.Label(text="Subnet Mask")
label2.grid(column=0, row=1, sticky="W")

# Entry Subnet
entry_field2 = tk.Entry()
entry_field2.grid(column=1, row=1, sticky="W")
entry_field2.insert(tk.END, '255.255.255.0')

# Label Gateway
label3 = tk.Label(text="Gateway")
label3.grid(column=0, row=2, sticky="W")

# Entry Gateway
entry_field3 = tk.Entry()
entry_field3.grid(column=1, row=2, sticky="W")
entry_field3.insert(tk.END, '192.168.0.1')

# Label Information
label4 = tk.Label(text="Note: The IP data populated\nis not your current IP data.\n")
label4.grid(column=0, row=4, sticky="W")

# Label Adapter
label5 = tk.Label(text="Adapter:", fg="red")
label5.grid(column=0, row=5, sticky="W")

# Label Adapter Connection
label6 = tk.Label(text="Local Area Connection", fg="red")
label6.grid(column=1, row=5, sticky="W")

#-- begin program   
window.mainloop()
