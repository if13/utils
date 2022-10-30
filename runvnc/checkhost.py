import socket
import os

#print(socket.gethostbyname('cleopatra.io'))
#print(socket.gethostbyaddr('192.168.0.58')[0])

def check_ping(host):
    response = os.system("ping -n 1 " + host)

    if response == 0:
        pingstatus = "ping ok"
    else:
        pingstatus = "network error"

    return pingstatus

#def reverse_host(host):
#    if all(i.isdigit() for i in host.split('.')):

