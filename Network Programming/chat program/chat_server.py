import socket

mysocket = socket.socket()

host = socket.gethostname() #return hostname
server_ip = socket.gethostbyname(host)
server_port = 4430
print(host, server_ip, ":", server_port)
mysocket.bind((host, server_port))


mysocket.listen()
while True:
    print("Waiting for client connection")
    client,client_ipaddress = mysocket.accept()
    print(client_ipaddress, "requested connection")
    
    while True:
        recieved_data = client.recv(1024)
        recieved_data = recieved_data.decode()
        # Process recieved data
        print("Client Msg:: ", recieved_data)
        if recieved_data.lower() == "quit":
            break
        # Send response to client
        response = input("Server: ")
        client.send(response.encode())