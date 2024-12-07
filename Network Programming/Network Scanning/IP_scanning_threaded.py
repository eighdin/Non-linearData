from tabnanny import verbose
from scapy.all import *
from scapy.layers.inet import *
import threading


def myping(ip_address):
    # Create an ICMP echo request packet
    icmp_pkt = IP(dst=ip_address)/ICMP()
    response_pkt = sr1(icmp_pkt, timeout=3, verbose=0)
    if response_pkt:
        print('got response')
        if response_pkt.getlayer("ICMP").type == 0:
            print(f'{ip_address} is REACHABLE')
    # else:
    #     print(f'bad ip :( {ip_address}')

def main():
    print("This is the main function")
    #target_ip_address = "10.51.0.2"
    #range: 10.51.0.1 - 10.51.0.254
    target_ip_prefix = '10.51.0.'
    for last_octet in range(1,255):
        target_ip_address = target_ip_prefix + str(last_octet)
        mythread = threading.Thread(target=myping, args=[target_ip_address])
        mythread.start()

main()