import socket
mysocket = socket.socket()

host = socket.gethostname()#returns host name
server_ip = socket.gethostbyname(host)
#server_ip = "10.51.80.123"
server_port = 4430
mysocket.connect((server_ip,server_port))
while True:
    weight = input("Enter Weight(lbs):")
    height = input("Enter height(inches):")

    msg = weight + " " + height
    mysocket.send(msg.encode())

    received_data = mysocket.recv(1024)
    print("BMI:",received_data.decode())
    cont = input("Do you want to continue (y/n):")
    if cont == "n":
        mysocket.send("quit".encode())
        break
