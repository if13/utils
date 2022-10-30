import PySimpleGUI as sg
import pandas as pd
import sys
from run_vnc2 import *
from load_file import *
from addr_autocomplite import *
from datetime import datetime
import socket
import platform
from checkhost import *
import os

sg.set_options(auto_size_buttons=True)



def save_data(data):
    with open('data', 'wb') as f:
        pickle.dump(data, f)
        
def load_data(data):
    with open('data', 'rb') as f:
        return pickle.load(data, f)

def get_time():
    cur_time_h = datetime.now().strftime("%H:%M:%S")
    return cur_time_h

def ping(host):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command) == 0

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

# Example
addToClipBoard('penny lane')



def gui_vnc():
    data = [] #инициализируем переменные
    # header_list = ['Филиал', 'Участок', 'Отдел', 'IP-адрес хоста', 'Имя хоста', 'ОС',
    #    'Проблемы, примечания', 'Железо', 'Принтер USB', 'Сетевой принтер',
    #    'Должность пользователя', 'ФИО', 'Город. линия',
    #    'Domain_user', 'admin_acc']
    search_list = ['IP-адрес хоста', 'Имя хоста', 'Должность пользователя', 
                  'ФИО', 'ГТС линия',  'Domain_user', 'Вн. номер']

    try:
        with open('data', 'rb') as f:
            df = pickle.load(f)
    except:
        df = load_file()

    data = df.values.tolist()
    search_list = df.columns.tolist()
    #print(search_list)

    layout = \
    [
      [sg.Input(do_not_clear=True, size=(15,1),enable_events=True, key='_INPUT1'),
         sg.Button('Run VNC', key='run_vnc1', size=(10,2)),
         sg.Text('   ',size = (3,1)),
         sg.Input(do_not_clear=True, size=(15,1),enable_events=True, key='_INPUT2'),
         sg.Button('Run VNC', key='run_vnc2', size=(10,2)),
         sg.Text('   ',size = (3,1)),
         sg.Input(do_not_clear=True, size=(15,1),enable_events=True, key='_INPUT3'),
         sg.Button('Run VNC', key='run_vnc3', size=(10,2)),
         sg.Text('   ',size = (3,1)),
         sg.Input(do_not_clear=True, size=(15,1),enable_events=True, key='_INPUT4'),
         sg.Button('Run VNC', key='run_vnc4', size=(10,2)),
         sg.Text('   ',size = (3,1)),
         sg.Input(do_not_clear=True, size=(15,1),enable_events=True, key='_INPUT5'),
         sg.Button('Run VNC', key='run_vnc5', size=(10,2))],

        [sg.Text('Search: ', key='_OUTPUT_', size = (8,1)),
          sg.Input(do_not_clear=True, size=(30,1),enable_events=True, key='_INPUT_'),
          sg.Button('check host', key='_CHECK_', size=(10, 2)),
          sg.Button('Run_VNC', key='runvnc', size=(10, 2)),
        ],

        #table element
        [sg.Table(values=data,
                  headings=df.columns.tolist(),
                  display_row_numbers=False,
                  auto_size_columns=True,
                  num_rows=min(20, len(data)),
                  right_click_menu = ['Unused', ['Run', 'Check', 'Copy username']],
                  key = '_TABLE_',
                  font=('Verdana', 8)),
         sg.Multiline(size=(65, 22), key='_LOG', font=('Verdana', 8))],

        [sg.Button('Add from file') , sg.Button('Save data')],
        #[sg.Text('')],
        [sg.Button('Exit')],
    ]

    window = sg.Window('tvnc_runner', layout, grab_anywhere=False)

    window.read()

    print(f'Всего записей известно: {len(df)}')
    msg = f'Всего записей известно: {len(df)}'
    window['_LOG'].update(msg+'\n', append=True)

    for search_col in search_list:
        if search_col not in df.columns: 
            print(f'Нет колонки для поиска: {search_col}')
            

    while True:
        event, values = window.read()
        df_s = pd.DataFrame()

        if event == 'Add from file':
            df = pd.concat([df, load_file()], axis = 0)
            window.Element('_TABLE_').Update(df.values.tolist())
        
        if event == 'Save data':
            save_data(df)


        if values['_INPUT_'] != '' and len(df):
            search = values['_INPUT_']
            print(search)
            for col in search_list:
                #print(df_s.append(df[df[col].str.contains(search, case=False)]))
                #print(col)
                df_s = df_s.append(df[df[col].str.contains(search, case=False)])
                #print('---update---')

            window.Element('_TABLE_').Update(df_s.values.tolist())

        else:
            df_s = df


        if 'run_vnc' in event:
            #runvnc(values['_INPUT_'])
            but_num = event[-1]
            #print((values[f'_INPUT{but_num}']))
            runvnc(addr_auto(values[f'_INPUT{but_num}']))
            cur_addr =  addr_auto(values[f'_INPUT{but_num}'])
            cur_hostname = socket.getfqdn(cur_addr)
            msg = f'{get_time()} {cur_addr} {cur_hostname}'
            window['_LOG'].update(msg+'\n', append=True)

        #запустить ВНЦ из контекст меню
        if event == 'Run':
            cur_addr = df_s.iloc[values['_TABLE_']]['IP-адрес хоста'].values[0]
            runvnc(cur_addr)
            #cur_addr = addr_auto(str(ip_ad[0]))
            cur_hostname = socket.getfqdn(cur_addr)
            msg = f'{get_time()} RUN:  {cur_addr} = {cur_hostname}'
            window['_LOG'].update(msg+'\n', append=True)

        #проверка из контекст меню
        if event == 'Check':
            ip_ad = df_s.iloc[values['_TABLE_']]['IP-адрес хоста'].values
            print(df_s.iloc[values['_TABLE_']].values)
            cur_addr = addr_auto(str(ip_ad[0]))
            cur_hostname = socket.getfqdn(cur_addr)
            msg = (f"{get_time()} CHECK:  {cur_addr} = {cur_hostname} - {check_ping(cur_addr)}")
            window['_LOG'].update(msg+'\n', append=True)

        if event == 'Copy username':
            cur_user = df_s.iloc[values['_TABLE_']]['Domain_user'].values[0]
            addToClipBoard(cur_user)

        #кнопка Check
        if event == '_CHECK_':
            cur_addr = addr_auto(search)
            cur_hostname = socket.getfqdn(cur_addr)
            msg = (f"{get_time()} CHECK:  {cur_addr} = {cur_hostname} - {check_ping(cur_addr)}")
            window['_LOG'].update(msg + '\n', append=True)

        if event == 'runvnc':
            runvnc(addr_auto(search))
            cur_addr = addr_auto(search)
            cur_hostname = socket.getfqdn(cur_addr)
            msg = (f"{get_time()} RUN:  {cur_addr} = {cur_hostname}")
            window['_LOG'].update(msg+'\n', append=True)


        if event == sg.WIN_CLOSED or event == 'Exit':
            save_data(df)
            window.close()
            break

gui_vnc()