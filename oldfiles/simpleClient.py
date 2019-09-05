import socket, _thread, easygui, uuid, sys



host =  "127.0.0.1"
port = 5000



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(b"ALIAS")
s.send(str(uuid.uuid4()).encode())


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
        

_thread.start_new(tx_thread, ())

while run:
    c = s.recv(1024)
    c = c.decode()
    print(c)
