import socket
mysocket = socket.socket()

host = socket.gethostname()#returns host name
server_ip = socket.gethostbyname(host)
server_port = 4444
mysocket.connect((server_ip,server_port))
while True:
    input_operator = input("Enter a math operator (+,-,*,/): ")
    input_number_one = input("Enter the first number: ")
    input_number_two = input("Enter the second number: ")

    msg =  f'{input_operator};{input_number_one};{input_number_two}'
    mysocket.send(msg.encode())

    received_data = mysocket.recv(1024)
    print("Result:",received_data.decode())
    cont = input("Do you want to continue (y/n):")
    if cont == "n":
        mysocket.send("quit".encode())
        break
