import pandas as pd
from tabulate import tabulate
from IPython.display import display, HTML
import PySimpleGUI as sg


def read_df():
    
    sheet_name='Сводная инф по ПК и юзерам'
    filename = sg.popup_get_file(
    'filename to open', no_window=True, file_types=(("Excel Files", "*.xls*"),))
    
    df = pd.read_excel(filename, 
                   sheet_name=sheet_name, 
                   index_col=4, 
                   )
    df.drop(columns = ['IP-телефон', 'TightVNC', 'KES', 'Aster', 'Нужна замена', 'Вн. номер'], inplace=True)
    
    print(df.index)
    print(df.columns)
    
    return df

read_df()









#print(df.head(2))
#df.loc[['kam-dir'], ['Вн. номер']] = "Жопушка"
#print(df.loc[['kam-dir'], ['Вн. номер']])
#print(df.iloc[3:10, 2:4])
#print((df.loc[df['IP-адрес хоста'].isin(['192.168.100.10'])]).to_list())











