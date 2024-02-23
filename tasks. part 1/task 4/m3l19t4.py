'''
Задача 4

Найти самое длинное слово в строке и вернуть его

'''

def find_longest_word(input_string):
    words = input_string.split(' ')
    longest_word = ''
    for word in range(len(words)):
        if word >= longest_word:
            longest_word = word

# Пример использования:
input_str = 'Тело управляет мыслью. Нужно организовать жизнь таким образом, чтобы , чтобы не давать телу рычаги управления собой.'
print(find_longest_word(input_str))
