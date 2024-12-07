import socket

mysocket = socket.socket()

host = socket.gethostname() #return hostname
server_ip = socket.gethostbyname(host)
#server_ip = "10.52.83.191"
server_port = 4430
print(host, server_ip, ":", server_port)
mysocket.connect((server_ip,server_port))

while True:
    weight = input("Enter weight(lbs): ")
    height = input("Enter height(in): ")
    msg = ' '.join([weight,height])
    mysocket.send(msg.encode())
    print("sending message: ", msg)
    # Recieving message from server
    recieved_data = mysocket.recv(1024)
    print("Server Msg -- BMI: ", recieved_data.decode())
    cont = input("Do you want to continue(y/n)? ")
    if cont.lower() == 'n':
        mysocket.send("quit".encode())
        break