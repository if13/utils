import subprocess
import pickle
from pathlib import Path



def runvnc(addr: str):
    
    dir_path = str(Path().absolute())
    vnc_path = r'"C:\Program Files\TightVNC\tvnviewer.exe" -optionsfile=' 
    file_name = 'temp.vnc'
    psw = ''

    data = {'ecb053cd1961cb22': ['192.168.0.','192.168.1.', '192.168.2.'],
            'de335672de23d203': ['192.168.10'], 
            '178919ca3c00eaaf': ['192.168.11'],
            '43c205a8e7a03160': ['192.168.12'],
            'ca868c0f2c0d8d84': ['192.168.13'], 
            '69969df553ff61fa': ['10.11.12.', '10.11.13.', '192.168.15']}

    for k, v in data.items():
        for _ in v:
            if _ in addr:
                psw = k
                break
    if not psw:
        psw = 'ecb053cd1961cb22'

    # with open('data.p', 'rb') as f: #get vnc cred
    #     data = pickle.load(f)
    #     print(data)


    with open(r'D:\py_ex\runvnc\template') as f:
        conn_info = f.readlines()
        conn_info[1] = f'host={addr}\n'
        conn_info[2] =  f'password={psw}\n'



    with open(r'D:\py_ex\runvnc\temp.vnc', 'wt') as f:
        f.writelines(conn_info)

    run_cmd = vnc_path + dir_path +'\\'+ file_name
    proc = subprocess.Popen(run_cmd)
    #удалить темп
