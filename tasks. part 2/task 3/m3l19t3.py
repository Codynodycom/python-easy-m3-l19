'''
Задача 3
"Переводчик азбуки Морзе"

Условие:
Напишите программу на Python, которая принимает на вход строку текста и переводит ее в азбуку Морзе. 
Программа должна поддерживать перевод букв латинского алфавита (в верхнем и нижнем регистрах) и 
цифр от 0 до 9. Все остальные символы, включая пробелы, должны игнорироваться.

Пример:

>>> Введите текст: Hello, World!
>>> Перевод в азбуку Морзе: .... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--

Объяснение:
Буквы и цифры заменены на соответствующие им символы азбуки Морзе. Пробелы оставлены в виде разделителей между словами.
'''

russian_alphabet = {
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'д': 'd',
    'е': 'e',
    'ё': 'yo',
    'ж': 'zh',
    'з': 'z',
    'и': 'i',
    'й': 'y',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ф': 'f',
    'х': 'kh',
    'ц': 'ts',
    'ч': 'ch',
    'ш': 'sh',
    'щ': 'shch',
    'ъ': '',
    'ы': 'y',
    'ь': '',
    'э': 'e',
    'ю': 'yu',
    'я': 'ya'
}

english_alphabet = {
    'a': 'эй',
    'b': 'би',
    'c': 'си',
    'd': 'ди',
    'e': 'и',
    'f': 'эф',
    'g': 'джи',
    'h': 'эйч',
    'i': 'ай',
    'j': 'джей',
    'k': 'кей',
    'l': 'эл',
    'm': 'эм',
    'n': 'эн',
    'o': 'оу',
    'p': 'пи',
    'q': 'кью',
    'r': 'ар',
    's': 'эс',
    't': 'ти',
    'u': 'ю',
    'v': 'ви',
    'w': 'дабл ю',
    'x': 'экс',
    'y': 'уай',
    'z': 'зед'
}

morze_alphabet = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..'
}

