'''
Задача 1
(изучи код и разбери как он работает)

Удалить все символы 'a' из строки и вывести результат
'''

def filter_string(input_string):
    filtered_string = ''
    for char in input_string:
        if char != 'a':
            filtered_string += char
    return filtered_string

# Пример использования:
input_str = 'banana'
print(filter_string(input_str))
