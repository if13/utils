import sys  
if sys.version_info[0] >= 3:  
    import PySimpleGUI as sg  
else:  
    import PySimpleGUI27 as sg  

layout = [[sg.Text('Your typed chars appear here:'), sg.Text('', key='_OUTPUT_', size=(40,1)) ],  
          [sg.Input(do_not_clear=True, key='_IN_')],  
          [sg.Button('Show'), sg.Button('Exit'), sg.Button('smf')],
          [sg.Output(key='_OUT_')], 
          ]  

window = sg.Window('Window Title').Layout(layout)  
print(window)

while True:                 # Event Loop  
  event, values = window.Read()  
  #print(event, values)
  if event is None or event == 'Exit':  
      break  
  if event == 'Show':  
      window.FindElement('_OUTPUT_').Update(values['_IN_'])
      print(values)
  if event == 'smf':  
      print('pressed show')
      window.FindElement('_OUT_').Update('asd')

window.Close()
