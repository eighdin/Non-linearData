from multiprocessing import Value
from scapy.all import *
from scapy.layers.inet import *
import threading
import queue
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
ping_timeout = 3
scan_timeout = 3
def portScan(ip_addr, tcp_port):
    # create TCP SYN packet
    tcp_pkt = IP(dst=ip_addr)/TCP(dport=tcp_port)
    # Sending and recieving TCP packets
    response = sr1(tcp_pkt, timeout=scan_timeout, verbose=0)
    # Displaying reponse
    if response:
        if response.getlayer(TCP).flags == "SA":
            print(tcp_port, "is OPEN")
        # else:
        #     print(tcp_port, "is CLOSED")
        #print(tcp_port, response.getlayer(TCP).flags)
    # else: # In case we do not receive any response
    #     print(f'{tcp_port} is FILTERED')

def myping(ip_address, result_q, active_host_count):
    # Create an ICMP echo request packet
    icmp_pkt = IP(dst=ip_address)/ICMP()
    response_pkt = sr1(icmp_pkt, timeout=ping_timeout, verbose=0)
    if response_pkt:
        if response_pkt.getlayer("ICMP").type == 0:
            #print(f'{ip_address} is REACHABLE')
            result_q.put((True, ip_address))
            with active_host_count.get_lock():
                active_host_count.value += 1
        else:
            result_q.put((False, ip_address))
    else:
        result_q.put((False, ip_address))

def main():
    active_host_num = Value('i', 0)
    target_ip_prefix = "10.54.32."
    port_range = 2000
    ip_range = 254
    result_queue = queue.Queue()
    print("Pinging", end='')
    
    for last_octet in range(1,ip_range):
        target_ip_address = target_ip_prefix + str(last_octet)

        ping_thread = threading.Thread(target=myping, args=[target_ip_address, result_queue, active_host_num])
        ping_thread.start()
        print('.', end='')
    
    print(f"\nDONE PINGING -- Starting Port Scan for {active_host_num.value} ACTIVE Hosts -- DONE PINGING")
    
    for last_octet in range(1, ip_range):
        ping_result = result_queue.get()
        
        if ping_result[0]:
            print(f'{ping_result[1]} is ACTIVE:\nPorts opened:')
            for target_port_num in range(1,port_range):
                port_thread = threading.Thread(target=portScan, args=[ping_result[1], target_port_num])
                port_thread.start()
            print(f'Done scanning IP: {ping_result[1]}\n')



if __name__ == "__main__":
    main()