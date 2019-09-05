# Tcp Chat server

import socket, select

connections = []
recv_buf = 4096
port = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("0.0.0.0", port))
server_socket.listen(10)

connections.append(server_socket)
#server_socket.connect((T))

print("Server started on port "+str(port))

def broadcast_data(sk, msg):
        for ssock in connections:
                if ssock != server_socket and ssock != sk:
                        #try:
                                ssock.send(msg)
                        #except:
                        #        ssock.close()
                        #        connections.remove(ssock)
                                

print(type(server_socket))

run = True
while run:
        #read_sockets, write_sockets, error_sockets = select.select(connections,[],[])

        for sock in connections:
                if sock == server_socket:
                        # Handle the case in which there is a new connection recieved through server_socket
                        try:
                                sockfd, addr = server_socket.accept()
                        except:
                                continue
                        connections.append(sockfd)
                        print("Client (%s, %s) connected" % addr)                               
                        broadcast_data(sockfd, "[%s:%s] entered room\n" % addr)
                else:
                        try:
                                data = sock.recv()
                                if data:
                                        broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)
                                        
                        except:
                                broadcast_data(sock, "Client (%s, %s) is offline")# % addr)
                                print("Client (%s, %s) is offline")# % addr)
                                sock.close()
                                connections.remove(sock)
                                continue
        server_socket.close()
                        


