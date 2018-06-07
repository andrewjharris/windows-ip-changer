import tkinter as tk
import os
import sys
import socket
from tkinter import *
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
window = tk.Tk()
window.title("Arlen's IP adjuster")
window.geometry("400x150")

#-- global variables
parts = ()
myip = str(IP)
mysub = ()
mygate = ()
ipdata = ()
lines = ()
f = ()

def chunk():
    os.system('cls')

def staticip():
	global myip
	global mysub
	global mygate
	global ipdata
	myip = str(entry_field1.get()).lower()
	mysub = str(entry_field2.get()).lower()
	mygate = str(entry_field3.get()).lower()
	set_static = ('netsh int ip set address "local area connection" static ' + str(myip.strip()) + " " + str(mysub.strip()) + " " + str(mygate.strip()) + ' 1')
	os.system(str(set_static))
def dynamicip():
	os.system('netsh int ip set address "local area connection" dhcp')
mydatda = str()
def print_to_file():
	global entry_field1
	global entry_field2
	global entry_field3
	global mydata
	global IP
	global mysub
	global mygate
	global lines
	global f
	ipdata = str('ipdata.txt')
	os.system('ipconfig > ipdata.txt')
	chunk()
	print("file '" + ipdata +"' created")
	f = open('ipdata.txt', "r")
	lines = f.readlines()
	IP = lines[7].split(": ")
	print(IP[1].strip())
	mysub = lines[8].split(": ")
	print(mysub[1].strip())
	mygate = lines[9].split(": ")
	print(mygate[1].strip())
	entry_field1.delete(0,tk.END)
	entry_field1.insert(tk.END, IP[1].strip())
	entry_field2.delete(0,tk.END)
	entry_field2.insert(tk.END, mysub[1].strip())
	entry_field3.delete(0,tk.END)
	entry_field3.insert(tk.END, mygate[1].strip())

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
entry_field1.insert(tk.END, str(myip))

# Label Subnet
label2 = tk.Label(text="Subnet Mask")
label2.grid(column=0, row=1, sticky="W")

# Entry Subnet
entry_field2 = tk.Entry()
entry_field2.grid(column=1, row=1, sticky="W")
entry_field2.insert(tk.END, str(mysub))

# Label Gateway
label3 = tk.Label(text="Gateway")
label3.grid(column=0, row=2, sticky="W")

# Entry Gateway
entry_field3 = tk.Entry()
entry_field3.grid(column=1, row=2, sticky="W")
entry_field3.insert(tk.END, str(mygate))


# Label Adapter
label5 = tk.Label(text="Adapter:", fg="red")
label5.grid(column=0, row=5, sticky="W")

# Label Adapter Connection
label6 = tk.Label(text="Local Area Connection", fg="red")
label6.grid(column=1, row=5, sticky="W")

# Get BUTTON
button3 = tk.Button(text="Get Current IP", command=print_to_file, width=18)
button3.grid(column=0, row=6, sticky="W")

#-- begin program   
print_to_file()
window.mainloop()
