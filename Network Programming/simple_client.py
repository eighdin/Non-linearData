import socket

mysocket = socket.socket()

host = socket.gethostname() #return hostname
#server_ip = socket.gethostbyname(host)
server_ip = "10.51.80.123"
server_port = 4430
mysocket.connect((server_ip,server_port))
msg = "I am mahesh"
mysocket.send(msg.encode())

recieved_data = mysocket.recv(1024)
print("server sent:", recieved_data.decode())