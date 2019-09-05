import socket, time
import _thread as thread

hostname = socket.gethostname()

recv_buf = 4096
port = 5000
server_socket = None

def Startup():
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen(10)
    thread.start_new(checker, ())
    logtxt.insert(INSERT, "Server started on port " + str(port) + ".\n")
    

#Startup()

connections = []

def checker():
    while 1:
        sockfd, addr = server_socket.accept()
        print("Accepted new connection")
        sockfd.settimeout(0.1)
        
        
        alias = sockfd.recv(20)[5:]
        sockfd.send(b"Hello, " + alias)
        

        broadcast(b"User " + alias + b" Has Joined!")
        connections.append([sockfd, addr, alias])

def broadcast(data):
    for conn in connections:
        try:
            conn[0].send(data)
        except:
            print("Failed to send to " + str(conn[1]))




run = True

  
def MainLoop():

    while run:

        print(len(connections))

        time.sleep(0.1)
        hasMessage = [None, None]
        for conn in connections:
            s = conn[0]
            try:
                pass#s.recv_into
            except:
                print("A client has disconnected!")
                logtxt.insert(INSERT, "A client has disconnected.\n")
                broadcast(b"A client has disconnected.")
                connections.remove(conn)

            try:
                b = s.recv(1024)
                print(str(conn[1]) + " said " + str(b))
                logtxt.insert(INSERT, str(conn[1]) + " said " + str(b) + "\n")
                hasMessage = [conn[2], b]
            except:
                pass

        if hasMessage != [None, None]:

            print("Broadcasting Message: " + str(hasMessage[1]))
            logtxt.insert(INSERT, "Broadcasting Message: " + str(hasMessage[1]) + "\n")

            for conn in connections:
                if conn[2] != hasMessage[0]:
                    # The user alias is different.
                    try:
                        conn[0].send(hasMessage[0] + b" said: " + hasMessage[1])
                    except:
                        connections.remove(conn)
                else:
                    conn[0].send(b"You:" + hasMessage[1])

            hasMessage = [None, None]

#MainLoop()
def Shutdown():
    global run
    run = False
    time.sleep(0.25)
    server_socket.close()
    sys.exit()



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

def initall():
    port = gPortNumber.get()
    Startup()
    thread.start_new(MainLoop, ())
 
new_item = Menu(menu) 
new_item.add_command(label='Start', command=initall)  
new_item.add_command(label='Stop', command=Shutdown)#, state = 'disabled')
new_item.add_separator()
new_item.add_command(label='Quit')
menu.add_cascade(label='File', menu=new_item)
 
window.config(menu=menu)

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
startButton = Button(tab1, text = "Start Server", command=initall)
shutdownButton = Button(tab1, text="Stop Server", command=Shutdown)



portLabel.grid(column = 0, row = 1)
portSpin.grid(column = 1, row = 1)
usersLabel.grid(column = 0, row = 2)
usersSpin.grid(column = 1, row = 2)
adressText.grid(column = 0, row = 4)
adressTextLong.grid(column = 0, row = 5)
adressTextIP.grid(column = 0, row = 7)
startButton.grid(column = 0, row = 8)
shutdownButton.grid(column = 1, row = 8)






logtxt = scrolledtext.ScrolledText(tab2, width = 80, height = 10)
logtxt.delete(1.0, END)



def clrLog():
    logtxt.delete(1.0, END)


clrBtn = Button(tab2, text="Clear Log", command = clrLog)

logtxt.grid(column = 0, row = 0)
clrBtn.grid(column = 0, row = 1)
 
tab_control.pack(expand=1, fill='both')
 
window.mainloop()
print("Finished")

