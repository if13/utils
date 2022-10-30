import socket

def addr_auto(addr: str):
    n_addr = len(addr.split('.'))
    if addr[0].isalpha():
        print(addr)
        print('this is name, not IP')
        try:
            return socket.gethostbyname(addr)
        except:
            return 'unresolved name'

    if n_addr == 1:
        addr = '192.168.0.' + addr
    if n_addr == 2:
        addr = '192.168.' + addr
    print(addr)
    return addr        
        

