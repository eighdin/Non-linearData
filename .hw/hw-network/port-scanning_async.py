import asyncio
from itertools import count
from scapy.all import *
from scapy.layers.inet import *
import logging
import queue

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

async def port_scan(ip_addr, tcp_port):
    # Create TCP SYN packet
    tcp_pkt = IP(dst=ip_addr)/TCP(dport=tcp_port)
    # Sending and receiving TCP packets
    response = await asyncio.to_thread(sr1, tcp_pkt, timeout=1, verbose=0)
    # Displaying response
    if response and response.getlayer(TCP).flags == "SA":
        print(f"{tcp_port} is OPEN")

async def myping(ip_address):
    # Create an ICMP echo request packet
    icmp_pkt = IP(dst=ip_address)/ICMP()
    response_pkt = await asyncio.to_thread(sr1, icmp_pkt, timeout=1, verbose=0)
    
    if response_pkt and response_pkt.getlayer("ICMP").type == 0:
        return True, ip_address
    else:
        return False, ip_address

async def main():
    target_ip_prefix = "10.54.32."
    port_range = 2000
    ip_range = 254

    ping_tasks = []
    
    for last_octet in range(1, ip_range):
        target_ip_address = target_ip_prefix + str(last_octet)
        ping_tasks.append(myping(target_ip_address))
    
    results = await asyncio.gather(*ping_tasks)
    print(len([entry for entry in results if entry[0]]))
    print(f"\nDONE PINGING -- Starting Port Scan for ACTIVE Hosts -- DONE PINGING")
    
    for ping_result in results:
        if ping_result[0]:  # If the host is active
            print(f'{ping_result[1]} is ACTIVE:\nPorts opened:')
            port_scan_tasks = [port_scan(ping_result[1], target_port_num) for target_port_num in range(1, port_range)]
            await asyncio.gather(*port_scan_tasks)
            print(f'Done scanning IP: {ping_result[1]}\n')

if __name__ == "__main__":
    asyncio.run(main())
