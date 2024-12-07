import socket

mysocket = socket.socket()

host = socket.gethostname() #return hostname
#server_ip = socket.gethostbyname(host)
server_ip = "10.52.83.191"
server_port = 4430
print(host, server_ip, ":", server_port)
mysocket.connect((server_ip,server_port))

while True:
    msg = input("Client: ")
    mysocket.send(msg.encode())
    if msg.lower() == "quit":
        break
    # Recieving message from server
    recieved_data = mysocket.recv(1024)
    print("Server Msg:: ", recieved_data.decode())