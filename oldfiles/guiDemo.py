from tkinter import *
 
from tkinter import Menu
from tkinter import ttk
from tkinter import scrolledtext
import socket
 
window = Tk() 
window.title("CHATTER SERVER")
#window.geometry("300x500")

gPortNumber = IntVar()
gPortNumber.set(5000)

gMaxUsers = IntVar()
gMaxUsers.set(100)
 
menu = Menu(window)
 
new_item = Menu(menu) 
new_item.add_command(label='Start')  
new_item.add_command(label='Stop')#, state = 'disabled')
new_item.add_separator()
new_item.add_command(label='Quit')
menu.add_cascade(label='File', menu=new_item)
 
window.config(menu=menu)
4
tab_control = ttk.Notebook(window)
 
tab1 = ttk.Frame(tab_control) 
tab2 = ttk.Frame(tab_control)
 
tab_control.add(tab1, text='Server Config') 
tab_control.add(tab2, text='Log')

lbl1 = Label(tab1, text= 'Server Configuration Settings') 
lbl1.grid(column=0, row=0)

portSpin = Spinbox(tab1, from_=1, to=9999, width = 8, textvariable=gPortNumber)
portLabel = Label(tab1, text="Port: ")
usersSpin = Spinbox(tab1, from_=3, to=300, width = 6, textvariable=gMaxUsers)
usersLabel = Label(tab1, text="Max Users: ")
adressText = Label(tab1, text="Connect to this server with these adresses:")
adressTextLong = Label(tab1, text=str(socket.gethostname()))
adressTextIP = Label(tab1, text = str(socket.gethostbyname(socket.gethostname())))
startButton = Button(tab1, text = "Start Server")#, command=None)



portLabel.grid(column = 0, row = 1)
portSpin.grid(column = 1, row = 1)
usersLabel.grid(column = 0, row = 2)
usersSpin.grid(column = 1, row = 2)
adressText.grid(column = 0, row = 4)
adressTextLong.grid(column = 0, row = 5)
adressTextIP.grid(column = 0, row = 7)
startButton.grid(column = 0, row = 8)






logtxt = scrolledtext.ScrolledText(tab2, width = 45, height = 10)
logtxt.delete(1.0, END)
logtxt.insert(INSERT, "Text is here")


def clrLog():
    logtxt.delete(1.0, END)


clrBtn = Button(tab2, text="Clear Log", command = clrLog)

logtxt.grid(column = 0, row = 0)
clrBtn.grid(column = 0, row = 1)
 
tab_control.pack(expand=1, fill='both')
 
window.mainloop()
print("Finished")
