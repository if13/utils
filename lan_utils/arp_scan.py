import sys
from datetime import datetime
from scapy.all import srp, Ether, ARP, conf
import socket

def get_port_access():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('192.9.200.124', 10050))
    if result == 0:
       print("Port is open")
    else:
       print("Error port access")
       print('!!!!!!!!!!!!!!!!!!!!')

    sock.close()


def arp_scan(interface, ips):

	print(f"[*] Scanning range {ips}...")
	start_time = datetime.now()

	conf.verb = 0
	ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ips),
		     timeout = 1,
		     iface = interface,
		     inter = 0.1)
	print('==================')
	print("[*] IP - NAME - MAC")
	for snd,rcv in ans:
		ip = rcv.sprintf("%ARP.psrc%")
		mac = rcv.sprintf("%Ether.src%")
		try:
			print('begin dns query')
			name = socket.gethostbyaddr(ip)[0]
		except:
			name = 'Not found'
		print(f'{ip} - {name} - {mac}')
		#print(rcv.sprintf("%ARP.psrc% - %Ether.src%"))



	stop_time = datetime.now()
	total_time = stop_time - start_time
	print("\n[*] Scan Complete. Duration:", total_time)

if __name__ == "__main__":
    #arp_scan(sys.argv[1], sys.argv[2])
	#arp_scan('local', '192.9.200.0/24')
	arp_scan('local', '10.80.90.0/24')


