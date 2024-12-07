import socket
import threading

def handle_client(client):
    while True:
        received_data = client.recv(1024)
        # Process the received data
        received_data = received_data.decode()
        print("Client sent:", received_data)
        if received_data == "quit":
            break
        values = received_data.split(";")
        client_operator = values[0]
        client_number_one = int(values[1])
        client_number_two = int(values[2])
        client_expression = f'{client_number_one}{client_operator}{client_number_two}'
        if client_operator in ["+","-","*","/"] and isinstance(client_number_one, int) and isinstance(client_number_two, int):
            msg = f'{eval(client_expression)}'
        else:
            msg = "dude, cmon"
        # Send the response to the client
        client.send(msg.encode())

def main():
    #Creating a socket
    mysocket = socket.socket()
    host = socket.gethostname()#returns host name
    ipaddress = socket.gethostbyname(host)# gethostname() takes host name and returns ip address
    port = 4444
    #Binding the socket with ip address (or hostname) and port
    mysocket.bind((host, port))
    #Keeping the server socket in listen mode
    mysocket.listen()
    while True:
        print("Waiting for a client connection")
        client,client_ipaddress = mysocket.accept()
        print(client_ipaddress,"requested connection")
        #handle_client(client)
        client_thread = threading.Thread(target=handle_client, args=[client])
        client_thread.start()



main()