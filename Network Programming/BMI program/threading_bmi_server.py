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
        values = received_data.split()
        weight = int(values[0])
        height = int(values[1])
        bmi = 703 * (weight / (height ** 2))
        bmi = str(bmi)
        # Send the response to the client
        # response = "Received"
        client.send(bmi.encode())

def main():
    #Creating a socket
    mysocket = socket.socket()
    host = socket.gethostname()#returns host name
    ipaddress = socket.gethostbyname(host)# gethostname() takes host name and returns ip address
    port = 4430
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