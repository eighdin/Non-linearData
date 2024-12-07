import socket
import threading

def handle_client(client):
    print("hit line 5")
    recieved_data = client.recv(1024)
    recieved_data = recieved_data.decode()
    print("recieved data")
    # Process recieved data
    print("Client Msg:: ", recieved_data)
    weight, height = recieved_data.split()
    weight = int(weight)
    height = int(height)
    bmi = 703 * (weight/(height**2))
    
    # Send response to client
    response = str(bmi)
    client.send(response.encode())

def main():
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
        # threading
        client_thread = threading.Thread(target=handle_client, args=[client])
        client_thread.start()
main()