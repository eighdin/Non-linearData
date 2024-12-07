import socket

mysocket = socket.socket()

host = socket.gethostname() #return hostname
server_ip = socket.gethostbyname(host)
server_port = 4430
mysocket.bind((host, server_port))
print(host, server_ip, ":", server_port)

mysocket.listen()
while True:
    client,client_ipaddress = mysocket.accept()
    print(client_ipaddress, "requested connection")
    recieved_data = client.recv(1024)
    
    print("Client sent:", recieved_data.decode())
    client.send("recieved message".encode())