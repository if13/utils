import os
import tabulate
from pd_part import *
from  run_vnc import *
import PySimpleGUI as sg

ipadrs = list(df['IP-адрес хоста'])
pc_names = list(df.index)
#print(pc_names)
#users = list(df['ФИО '])

layout = [  [sg.Text('Your typed chars appear here:')],
            [sg.Text('', key='_OUTPUT_', size = (20,1))],
            [sg.Input(do_not_clear=True, size=(20,1),enable_events=True, key='_INPUT_')],
            [sg.Listbox(ipadrs, size=(50, 10), enable_events=True, key='_LIST_')],
            [sg.Button('Runvnc'), sg.Button('Exit')]]

window = sg.Window('TightVNC runner').Layout(layout)
# Event Loop
while True:
    event, values = window.Read()
    if event is None or event == 'Exit':                # always check for closed window
        break
    if values['_INPUT_'] != '':                         # if a keystroke entered in search field
        search = values['_INPUT_']
        new_values = [x for x in ipadrs if search in x]  # do the filtering
        window.Element('_LIST_').Update(new_values)     # display in the listbox
        window.FindElement('_OUTPUT_').Update(values['_INPUT_'])

    else:
        window.Element('_LIST_').Update(ipadrs)          # display original unfiltered list
    if event == '_LIST_' and len(values['_LIST_']):     # if a list item is chosen
        sg.Popup('Selected ', tabulate(df.loc[df['IP-адрес хоста'].isin(values['_LIST_'])],
                headers='keys', tablefmt="github", numalign="right"),
                line_width=350, font=('Helvetica', 6) 
                )
    if event == 'Runvnc':
        print(values['_LIST_'])
        #runvnc(values['_LIST_'])
    

window.Close()
