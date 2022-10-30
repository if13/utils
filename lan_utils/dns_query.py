#import dnspython as dns
import time
import dns.resolver
import getmac
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

test_mac = getmac.get_mac_address(ip="192.9.200.124"
                                     "", network_request=True)
print(test_mac)

for i in range (1000):
    result = dns.resolver.query('fileserver.trei.gmbh', 'A')
    get_port_access()
    time.sleep(2)
    for ipval in result:
        print('IP', ipval.to_text())
        mac = getmac.get_mac_address(ip="192.9.200.124", network_request=True)
        print(mac)
        if test_mac != mac:
            print('!!!!!!!!!')
            print(mac, test_mac)
            time.sleep(10000)
    print('iteration N ', i)
    print('-----------')
