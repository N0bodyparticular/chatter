# telnet program example
import socket, select, string, sys, easygui
import _thread as thread

#s = None

def prompt_thread():
    while 1:
        textToSay = easygui.enterbox("Message:")
        print("TX: " + textToSay)
        s.send(textToSay)
        

host =  "DESKTOP-G1845UN"
port = 5000


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#s.settimeout(5)


s.connect((host, port))
try :
        pass#s.connect((host, port))
except :
        print('Unable to connect')
        sys.exit()

print("Connected to Server...")

thread.start_new(prompt_thread, ())

while 1:
    s.send(b"Hello, World")
    data = s.recv(4096)
    if not data :
            print('\nDisconnected from chat server')
            sys.exit()
    else :
            #print data
            print(data)
            
            
			





"""def prompt() :
	sys.stdout.write('<You> ')
	sys.stdout.flush()

#main function
if __name__ == "__main__":
	
	if(len(sys.argv) < 3) :
		print('Usage : python telnet.py hostname port')
		sys.exit()
	
	host = sys.argv[1]
	port = int(sys.argv[2])
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)
	
	# connect to remote host
	try :
		s.connect((host, port))
	except :
		print('Unable to connect')
		sys.exit()
	
	print('Connected to remote host. Start sending messages')
	prompt()
	
	while 1:
		socket_list = [sys.stdin, s]
		
		# Get the list sockets which are readable
		read_sockets, write_sockets, error_sockets = [s, s, s]#select.select(socket_list , [], [])
		
		for sock in [s]:
			#incoming message from remote server
			if sock == s:
				data = sock.recv(4096)
				if not data :
					print('\nDisconnected from chat server')
					sys.exit()
				else :
					#print data
					sys.stdout.write(data)
					prompt()
			
			#user entered a message
			else :
				msg = sys.stdin.readline()
				s.send(msg)
				prompt()"""

