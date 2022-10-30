import PySimpleGUI as sg
import pandas as pd


def load_file():
   
    drop_list = ['Филиал', 'ОС', 'IP-телефон', 'TightVNC', 'KES', 'Aster', 
                 'Нужна замена', 'Проблемы, примечания', 'Сетевой принтер', 'Принтер USB', 
                 'Железо', 'Unnamed: 0', 'Unnamed: 0']
    filename = sg.popup_get_file(
    'filename to open', no_window=True, 
    file_types=(("Excel Files", "*.xls*"),))

    if filename == '':
        sg.popup_error('Ошибка указания файла')
        return


    if filename is not None:
        try:
            sheet_name='Сводная инф по ПК и юзерам' # 
            df = pd.read_excel(filename, sheet_name, dtype = object)
            df.fillna('-', inplace=True)

            for drop_col in drop_list:
                try:
                    df.drop(columns = [drop_col], inplace=True)
                except:
                    print(f'Нет колонки для очистки: {drop_col}')
                    pass

            
            df['Вн. номер'] = df['Вн. номер'].astype(str)
            data = df.values.tolist()
            print(df.columns)
            
        except Exception as e:
            sg.popup_error(e)

    return df

