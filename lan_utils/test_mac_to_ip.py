from datetime import datetime
from scapy.all import srp, Ether, ARP, conf
import socket




def arp_scan(interface, ips):

	print(f"[*] Scanning range {ips}...")
	start_time = datetime.now()

	conf.verb = 0
	ans, unans = srp(Ether(dst="00:22:CA:89:AE:5B"),
		     timeout = 1,
		     iface = interface,
		     inter = 0.1)
	print('==================')
	print("[*] IP - NAME - MAC")

	for snd, rcv in ans:
		ip = rcv.sprintf("%ARP.psrc%")
		mac = rcv.sprintf("%Ether.src%")

arp_scan('local', '10.80.90.0/24')
