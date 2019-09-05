import socket, _thread, easygui, uuid, sys
import pdb, time



host =  "127.0.0.1"
port = 5000
eventer = "None"
s = None

def threadsafe_send(message):
    global needToSend, stuffToSend
    needToSend = True
    stuffToSend  = message
    
senddata = None


def init():
    #pdb.set_trace()
    global host, port, s, senddata
    print("Getting hostname")
    host = nameBox.get()
    print("Getting Port")
    port = int(portSpin.get())
    print("Setting up socket")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Connecting socket")
    s.connect((host, port))
    print("Sending Data")
    senddata = (b"ALIAS" + str(uuid.uuid4()).encode())

def initall():
    global eventer
    eventer = "initall"
    print("Initialise pressed")

    
def initall_ev():
    init()
    _thread.start_new(mainloop, ())




##
##def loop1():
##    loop2()
##
##def loop2():
##    c = s.recv(1024)
##    c = c.decode()
##    print(c)
##    viewtxt.insert(INSERT, c)
##    loop1()


run = True
def tx_thread():
    global run
    while 1:
        text = easygui.enterbox("Message:")

        if text == None:
            s.close()
            run = False
            sys.exit()
            break

        s.send(text.encode())
        

#_thread.start_new(tx_thread, ())

def mainloop():
    while run:
        c = b'e'#s.recv(1024)
        c = c.decode()
        print(c)
        #viewtxt.insert(INSERT, c)
    


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

needToSend = False
stuffToSend = b''

def send_message(*args):
    global eventer
    eventer = "send_message"
    print("Send Message")


def send_message_ev(*args):
    print(message.get())
    s.send(message.get().encode())
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

startButton = Button(tab1, text = "Connect to Server", command = initall)#, command=None)



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

waitForConnect = True

def tx_safe():
    global senddata
    s.send(senddata)
    senddata = None
    time.sleep(0.1)

def mainControlLoop():
    global eventer, senddata
    
    print ("######STARTING THREAD LOOP##########")
    
    if eventer != "None":
        if eventer == "initall": initall_ev()
        if eventer == "send_message": send_message_ev()
        eventer = "None"

    if senddata != None:
        print ("Sending Data")
        window.after(2, tx_safe)
        print ("Sent Data")
        
        
    #if needToSend:
    #    needToSend = False
    #    s.send(stuffToSend)
    window.after(150, mainControlLoop)



window.after(350, mainControlLoop)
window.mainloop()
##






print("Finished")
