from tkinter import *

from tkinter import Menu
from tkinter import ttk
from tkinter import scrolledtext
import socket



window = Tk() 
window.title("CHATTER")
#window.geometry("300x500")

message = StringVar()
message.set('')


def send_message(*args):
    print(message.get())
    message.set('')
    
    


    
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

tab_control = ttk.Notebook(window)
 
tab1 = ttk.Frame(tab_control) 
tab2 = ttk.Frame(tab_control)
 
tab_control.add(tab1, text='Server') 
tab_control.add(tab2, text='Chat')

lbl1 = Label(tab1, text= 'Server Settings') 
lbl1.grid(column=0, row=0)

portSpin = Spinbox(tab1, from_=1, to=9999, width = 8, textvariable=gPortNumber)
portLabel = Label(tab1, text="Port: ")

nameBox = Entry(tab1)
nameLabel = Label(tab1, text="Server name/IP: ")

startButton = Button(tab1, text = "Connect to Server")#, command=None)



portLabel.grid(column = 0, row = 1)
portSpin.grid(column = 1, row = 1)
nameBox.grid(column = 1, row = 2)
nameLabel.grid(column = 0, row = 2)
startButton.grid(column = 0, row = 8)


viewtxt = scrolledtext.ScrolledText(tab2, width = 45, height = 10, state='disabled')
viewtxt.delete(1.0, END)
#viewtxt.insert(INSERT, "") # <- template 

messageEntry = Entry(tab2, textvariable = message)
messageEntry.bind("<Return>", send_message)
sendButton = Button(tab2, text = "Send", command=send_message)




def clrLog():
    viewtxt.delete(1.0, END)



viewtxt.grid(column = 0, row = 0)
messageEntry.grid(column = 0, row = 1)
sendButton.grid(column = 1, row = 1)


 
tab_control.pack(expand=1, fill='both')
 
window.mainloop()
print("Finished")
