import configparser
from wireguard_keys import *


PUB_KEY = '...' #здесь должен быть указан общий ключ

if __name__ == "__main__":

	try:
		with open('curr_ip_sip.txt', 'r') as f:
			IP_N = int(f.readline())
	except FileNotFoundError:
		IP_N = int(input('не найден последний IP, введите его вручную: '))

	#numbers of clients
	N = int(input('введите количество генерируемых конфигов: '))

	for i in range(1, N+1):

		cur_ip_sip = IP_N + i # increment IP-address
		(privkey, pubkey, sharkey) = generate_wireguard_keys()
		config = f'''[Interface]
PrivateKey = {privkey}
ListenPort = 51821
Address = 172.25.1.{cur_ip_sip}/24
DNS = 192.9.200.124, 192.9.200.132
#pubkey = {pubkey}
		
[Peer]
PublicKey = {PUB_KEY}
PresharedKey = {sharkey}
AllowedIPs = 172.25.1.0/24, 192.9.200.0/24, 192.168.11.0/24
Endpoint = ...:... #здесь должен быть указан внешний адрес подключения и порт
PersistentKeepalive = 5
'''

		name_config = input('введите дескрипшн конфига: ')

		with open(f'wg_sip_{cur_ip_sip}_{name_config}.conf', 'w') as f:
			f.write(config)

		print('-------------------------------------')
		print(f'ip: 172.25.1.{cur_ip_sip}')
		print(f'имя конфига: {name_config}_sip')
		print(f'pubkey: {pubkey}')
		print(f'sharkey: {sharkey}')
		print('-------------------------------------')
		print()

	#update last ip
	with open('curr_ip_sip.txt', 'w') as f:
		f.write(str(cur_ip_sip))



