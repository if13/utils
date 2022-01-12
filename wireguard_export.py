import subprocess
import configparser


def get_pubkey(privkey):
	bprivkey = bytes(privkey, 'utf-8')
	command = ['wg', 'pubkey']
	process = subprocess.Popen(command,
							   stdin=subprocess.PIPE,
							   stdout=subprocess.PIPE,
							   stderr=subprocess.STDOUT)
	pubkey = process.communicate(input=bprivkey)[0].decode("cp866")
	return pubkey

def generate_wireguard_keys():
	privkey = subprocess.check_output("wg genkey", shell=True).decode("utf-8").strip()
	pubkey = get_pubkey(privkey)
	sharkey = subprocess.check_output("wg genpsk", shell=True).decode("utf-8").strip()
	return (privkey, pubkey, sharkey)

print(generate_wireguard_keys())

if __name__ == "__main__":

	try:
		with open('curr_ip.txt', 'r') as f:
			IP_N = int(f.readline())
	except FileNotFoundError:
		IP_N = int(input('не найден последний IP, введите его вручную: '))

	#numbers of clients
	N = int(input('введите количество генерируемых конфигов: '))

	for i in range(1, N+1):
		cur_ip = IP_N + i
		(privkey, pubkey, sharkey) = generate_wireguard_keys()
		config = configparser.ConfigParser()
		config['Interface'] = {'PrivateKey': privkey,
							'ListenPort': '', #insert
							'Address':  f'172.26.1.{cur_ip}',
							'DNS': '192.9.200.124, 192.9.200.132',
							'#pubkey': f'{pubkey}'}

		config['Peer'] = {
		'PublicKey': '', #insert
		'PresharedKey': f'{sharkey}',
		'AllowedIPs': '172.26.1.0/24, 192.9.200.0/24, 192.168.11.0/24',
		'Endpoint': 'xx.xx.xx.xx:xxxxx' } #insert

		name_config = input('введите дескрипшн конфига: ')

		with open(f'wg_config_{cur_ip}_{name_config}.txt', 'w') as f:

			config.write(f)

	#update last ip
	with open('curr_ip.txt', 'w') as f:
		f.write(str(cur_ip))



