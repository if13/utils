''' 1. Как преобразовать строку, содержащую бинарный код (0 или 1), в число (целого
типа)? Напишите программу, которая будет это делать.'''


bite_string = "1011001"
x = int(bite_string, 2)
print('\nРезультат задачи 1')
print(x)    


''' 2. Как проверить, что кортеж A содержит в себе все элементы кортежа B? Напишите
программу, которая это будет выполнять.'''

a = (1, 2, 3, 4)
c = (1, 2, 10)
b = (1, 2, 2, 3)

#используем преобразования к множествам. Вхождение элементов без учета повторений
def all_in_it(first, last):
    return set(first).issubset(last) 

print('\nРезультат задачи 2 (без учета повторений)')
print(all_in_it(b, a)) # b не является подмножеством a, то есть не все элементы а содержатся в с
print(all_in_it(c, a)) # c является подмножество a, то есть все элементы b содержатся в с


#вхождение элементов с учетом повторений
def all_in_it_without_dupl(first, last):
    first_list = list(first)
    last_list = list(last)
    
    while len(first_list)>0:
        to_check = first_list[0] 
        if to_check not in last_list:
            return False
        first_list.remove(to_check)
        last_list.remove(to_check)
    
    return True
    
print('\nРезультат задачи 2 (с учетом повторений)')
print(all_in_it_without_dupl(b, a)) # b не является подмножеством с, с учетом повторяющихся значений


'''3. Как преобразовать строку в число, состоящее из ASCII-кодов? Напишите
программу для этой операции.'''

def string_to_ascii(word):
    return ''.join([str(ord(c)) for c in word])

print('\nРезультат задачи 3')
print(string_to_ascii('hello!'))


'''4. Как удалить пустые строки (длиной 0) из списка строк? Напишите программу для
этого. '''

def clear_list(lst):
    return [i for i in lst if len(i)>0]

print('\nРезультат задачи 4')
print(clear_list(['hello', '', 'word']))


'''5. Создайте строку из чисел от 0 до 100 следующего вида: "0123456789101112..." '''

def do_str():
    w = ''
    for i in range(0, 101):
        w += str(i)
    return w

print('\nРезультат задачи 5')
print(do_str())



'''6.  Преобразуйте список, где есть повторяющиеся элементы, в список, где все
элементы уникальны.'''

def get_unique(lst):
    return list(set(lst))

print('\nРезультат задачи 6')
print(get_unique(b)) 


'''7. Создайте список всех простых чисел, лежащих в диапазоне от 0 до 100. '''
def get_list_100():
    a = []
    for i in range(0, 101):
        a.append(i)
    return a

print('\nРезультат задачи 7')        
print(get_list_100())        


''' 8. Реализуйте код, который будет выводить в консоли числа от 1 до 100. Если число
кратно 4, то вместо числа выводить слово “Python”, если число кратно 6, то
выводить вместо числа слово “Django”, А если число кратно и 4 и 6, выводить
слово “SQL”'''

def get_mix_range():
    for i in range(0, 101):
        if i%4 == 0 and i%6 == 0:
            print('SQL')
            continue
        elif i%4 == 0:
            print('Python')            
        elif i%6 == 0:
            print('Django')
        else:
            print(i)
        
print('\nРезультат задачи 8')          
get_mix_range()
        
        
        
        
        
        
        

