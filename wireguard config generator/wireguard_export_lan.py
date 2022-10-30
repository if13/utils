import configparser
from wireguard_keys import *


PUB_KEY = '...' # здесь должен быть указан public key

if __name__ == "__main__":

	try:
		with open('curr_ip.txt', 'r') as f:
			IP_N = int(f.readline())
	except FileNotFoundError:
		IP_N = int(input('не найден последний IP, введите его вручную: '))

	#numbers of clients
	N = int(input('введите количество генерируемых конфигов: '))

	for i in range(1, N+1):

		cur_ip = IP_N + i # increment IP-address
		(privkey, pubkey, sharkey) = generate_wireguard_keys()
		config = configparser.ConfigParser()
		config['Interface'] = {
							'PrivateKey': privkey,
							'ListenPort': '51820',
							'Address':  f'172.26.1.{cur_ip}/24',
							'DNS': '192.9.200.124, 192.9.200.132',
							'#pubkey': f'{pubkey}'}
		config['Peer'] = {
		'PublicKey': f'{PUB_KEY}',
		'PresharedKey': f'{sharkey}',
		'AllowedIPs': '172.26.1.0/24, 192.9.200.0/24',
		'Endpoint': '...:...', # здесь должен быть указан внешний адрес и порт
		'PersistentKeepalive': 5
		}

		name_config = input('введите дескрипшн конфига: ')

		with open(f'wg_lan_{cur_ip}_{name_config}.conf', 'w') as f:
			config.write(f)

		print('-------------------------------------')
		print(f'ip: 172.26.1.{cur_ip}')
		print(f'имя конфига: {name_config}')
		print(f'pubkey: {pubkey}')
		print(f'sharkey: {sharkey}')
		print('-------------------------------------')
		print()

	#update last ip
	with open('curr_ip.txt', 'w') as f:
		f.write(str(cur_ip))



