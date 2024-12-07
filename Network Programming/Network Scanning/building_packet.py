from scapy.config import conf
conf.ipv6_enabled = False
from scapy.all import *
pkts = sniff(filter="ip and not ip6", count=3, store=0, iface="wlp2s0")
print(pkts)
