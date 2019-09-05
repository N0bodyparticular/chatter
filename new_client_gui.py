import socket, _thread, easygui, uuid, sys, select
import pdb, time
from tkinter import *
from tkinter import Menu
from tkinter import ttk
from tkinter import scrolledtext


host =  "127.0.0.1"
port = 5000
eventer = "None"
s = None

window = Tk() 
window.title("CHATTER")
#window.geometry("300x500")

message = StringVar()
message.set('')

s = None # Socket ref. In the init function it is set to a socket.


def connect():
    print("Connecting to server!")
    global host, port, s
    
    host = nameBox.get()
    port = int(portSpin.get())
    print("Params: Host=\""+ str(host) + "\", port="+str(port))
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        s.connect((host, port))
    except:
        print("Error connecting to server!")
        return
    print("Sending Data...")
    s.send(b"ALIAS" + str(aliasBox.get()).encode())
    print("Logon complete!")
    s.settimeout(0.3)

def send_message(*args):
    global viewtxt
    msg_text = message.get()
    print("Sending a message: " + msg_text)
    s.send(msg_text.encode())
    print("Message sent.")
    message.set("")
    #viewtxt.insert(END, "You: "+msg_text + '\n')


    
        
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

aliasBox = Entry(tab1)
aliasLabel = Label(tab1, text="Alias: ")



startButton = Button(tab1, text = "Connect to Server", command = connect)#, command=None)

portLabel.grid(column = 0, row = 1)
portSpin.grid(column = 1, row = 1)
nameBox.grid(column = 1, row = 2)
nameLabel.grid(column = 0, row = 2)
aliasLabel.grid(column = 0, row = 3)
aliasBox.grid(column = 1, row = 3)

startButton.grid(column = 0, row = 8)

viewtxt = scrolledtext.ScrolledText(tab2, width = 45, height = 10)#, state='disabled') #scrolledtext.ScrolledText(tab2, width = 45, height = 10, state='disabled')

messageEntry = Entry(tab2, textvariable = message)
messageEntry.bind("<Return>", send_message)
sendButton = Button(tab2, text = "Send", command=send_message)

def clrLog():
    viewtxt.delete(1.0, END)



viewtxt.grid(column = 0, row = 0)
messageEntry.grid(column = 0, row = 1)
sendButton.grid(column = 1, row = 1)



tab_control.pack(expand=1, fill='both')


def recv_loop(*args):
    if s!= None:
        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select([s], [s], [s])
        for sock in read_sockets:
        #incoming message from remote server
            if sock == s:
              c = sock.recv(4096)
              c = c.decode()
              if not c :
                print('\nDisconnected from server')
                sys.exit()
              else :
                 print(c, end='')
                 viewtxt.insert(END, "\n" + c)# + '\n')
                 viewtxt.see(END)
                 window.after(120, recv_loop)
    else:
        print("Waiting for connection")
    """
    if s != None:
        c = ''
        c = s.recv(1024)
        c = c.decode()
        
            
        print(c, end='')
        viewtxt.insert(END, "\n" + c + '\n')
        window.after(120, recv_loop)
            
        
        
    else: # when the socket isn't open yet, wait.
        print("Waiting for socket activation")"""
    window.after(500, recv_loop)

window.after(100, recv_loop)

window.mainloop()
