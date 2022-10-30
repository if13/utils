import pickle

# pnz = ['192.168.0.','192.168.1.']
# kam = ['192.168.10']
# lom = ['192.168.11']
# nik = ['192.168.12']
# ser = ['192.168.13']
# met = ['10.11.12.', '10.11.13.', '192.168.15']


data = {'el(aQ1&k': ['192.168.0.','192.168.1.'], 
        '54h<RTgf': ['192.168.10'] , 
        'H1(bnA7@': ['192.168.11'],
        'J43M!g5n': ['192.168.12'],
        'Kt^sb7Ad': ['192.168.13'], 
        'G5Hth^1N': ['10.11.12.', '10.11.13.', '192.168.15']}

# with open('conndata') as f:
#      data = f.readlines()
     


with open('data', 'wb') as f:
    pickle.dump(data, f)

with open('data', 'rb') as f:
     data_new = pickle.load(f)
     print(data_new)

