import socket
print("We're in tcp server...");
#select a server port
server_port = 12000
#create a welcoming socket
welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#bind the server to the localhost at port server_port
welcome_socket.bind(('3.89.138.43',server_port))
welcome_socket.listen(1)
#ready message
print('Server running on port ', server_port)
#Now the main server loop
while True:
 connection_socket, caddr = welcome_socket.accept()
 #notice recv and send instead of recvto and sendto
 cmsg = connection_socket.recv(1024)
 cmsg = cmsg.decode()
 if(cmsg.isalnum() == False):
    cmsg = "Not alphanumeric.";
 else:
    cmsg = "Alphanumeric";
 connection_socket.send(cmsg.encode()) 
