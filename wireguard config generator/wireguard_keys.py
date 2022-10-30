import subprocess


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