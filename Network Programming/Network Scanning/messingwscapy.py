from scapy.all import *
from scapy.layers.inet import *
from scapy.config import *

src_host = "10.51.4.52"
dest_host = "10.52.83.193"
# pkt = IP(dst=dest_host, src=src_host) / ICMP()

# response = sr1(pkt, timeout=5, verbose=0)
# if response:
#     if response.getlayer("ICMP").type == 0:
#         print(f'Recieved reply from: {dest_host}')
#     else:
#         print(response)

p = Ether(dst="ff:ff:ff:ff:ff:ff")