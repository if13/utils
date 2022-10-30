import socket
import subprocess
import ipaddress
import re

print('Задайте диапазон адресов.')

adresses = ['192.168.0.' + str(i) for i in range(int(input('введите начальный адрес: ')),
                                                 int(input('введите конечный адрес: ')) + 1)]
blank = []
with open(r'D:\getvnc\template') as f:
    blank = f.readlines()

for addr in adresses:
    args = f'WMIC /NODE: {addr} COMPUTERSYSTEM GET USERNAME'.strip()
    process = subprocess.run(args, stdout=subprocess.PIPE)

    try:
        login = re.search('GAZ\\\(.+)', process.stdout.decode('CP866'))[1]
        login = login.strip()
    except:
        login = None

    name = socket.getfqdn(addr)
    print([name])

    if login:
        with open(f'D:\getvnc\{login} - {name} - {addr}.vnc', 'wt') as f:
            cur_blank = blank
            cur_blank[1] = f'host={name}\n'
            f.writelines(cur_blank)
            print(f'сохранение файла: host={name}\n')






