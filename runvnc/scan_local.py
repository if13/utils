import socket
import subprocess
import re
import pandas as pd
import PySimpleGUI as sg

def do_scan():
    #сканирование сети  192.168.0.x/24
    start_addr = 50
    end_addr = 220
    adresses = ['192.168.0.' + str(i) for i in range(start_addr, end_addr+1)]

    filename = sg.popup_get_file('откройте файл импорта/шаблон столбцов', no_window=True,
                                 file_types=(("Excel Files", "*.xls*"),))
    sheet_name='Сводная инф по ПК и юзерам' # 

    df = pd.read_excel(filename, sheet_name=sheet_name,dtype=object)
    df.fillna('-', inplace=True)
    try:
        df.drop(columns=['IP-телефон', 'TightVNC', 'KES', 'Aster',
                       'Нужна замена', 'Проблемы, примечания', ], inplace=True)
    except:
        pass
    df['Вн. номер'] = df['Вн. номер'].astype(str)
    #dfscan = pd.DataFrame(columns=df.columns)

    #counters
    passed_n = 0
    added_n = 0
    deleted_n = 0

    for addr in adresses:
        print('---------------')
        print(addr+' >>> ', end='')
        compname = socket.getfqdn(addr)
        print('Имя ПК ', compname)

        if '192.' in compname:
            print('не найдено имя ПК ===================')
            continue
        target = df[df['IP-адрес хоста'] == addr]
        #print(target)

        if len(target) and target['Имя хоста'].item() == compname:
            print('уже есть, пропускаем =================== ')
            passed_n += 1
            continue
        if len(target) and target['Имя хоста'].item() != compname: #or not target['Domain_user'].item()):
            print('удаление неактуального адреса')
            df.drop(df[df['IP-адрес хоста'] == addr].index, inplace=True)
            deleted_n += 1

        #get domain user name
        print('начало выполнения запроса имени юзера')
        args = f'WMIC /NODE: {addr} COMPUTERSYSTEM GET USERNAME'.strip()
        process = subprocess.run(args, stdout=subprocess.PIPE)
        print('запрос завершен')

        try:
            username = re.search('GAZ\\\(.+)', process.stdout.decode('CP866'))[1]
            username = username.strip()
        except:
            username = None

        if username:
            df = pd.concat([df, pd.DataFrame.from_dict(
                {'Филиал': ['ЦО'],
                'IP-адрес хоста': [addr], 
                'Имя хоста': [compname],
                'Domain_user': [username]})], 
                axis = 0)
            added_n += 1
            print('добавлена строка', addr, compname, username)


    df.to_pickle('scandump')    
    df.to_excel('scandump.xls', sheet_name=sheet_name)   
    print(f'работа скрипта завершена. Добавлено записей: {added_n}, удалено: {deleted_n}, пропущено: {passed_n} ')
    print(f'сохранен в файл scandump.xls')
#
#

print('begin func')
do_scan()





