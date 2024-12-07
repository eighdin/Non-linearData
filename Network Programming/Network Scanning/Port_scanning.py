from scapy.all import *
from scapy.layers.inet import *
import threading

def portScan(ip_addr, tcp_port):
    # create TCP SYN packet
    tcp_pkt = IP(dst=ip_addr)/TCP(dport=tcp_port)
    # Sending and recieving TCP packets
    response = sr1(tcp_pkt, timeout=1, verbose=0)
    # Displaying reponse
    if response:
        if response.getlayer(TCP).flags == "SA":
            print(tcp_port, "is OPEN")
        else:
            print(tcp_port, "is CLOSED")
        print(tcp_port, response.getlayer(TCP).flags)
    # else: # In case we do not receive any response
    #     print(f'{tcp_port} is FILTERED')

def main():
    target_ip_address = "10.52.83.100"
    target_port_num = 135
    for target_port_num in range(1,30000):
        port_thread = threading.Thread(target=portScan, args=[target_ip_address, target_port_num])
        port_thread.start()

main()