'''
Задача 5
Допиши код

Вы хотите создать программу для шифрования сообщений с использованием шифра Виженера. Для этого вам нужно написать функцию, 
которая будет принимать сообщение и ключ шифра, а затем возвращать зашифрованное сообщение.

Шифр Виженера использует ключевое слово, чтобы определить сдвиг для каждой буквы в сообщении. Например, если ключевое 
слово - "python", то для первой буквы в сообщении будет использоваться сдвиг на 16 позиций (так как "p" - 16-я буква в 
алфавите), для второй буквы - сдвиг на 24 позиции (так как "y" - 24-я буква в алфавите), и так далее.

Вам нужно написать функцию vigenere_cipher(message, keyword), которая будет принимать сообщение и ключевое слово, а 
затем возвращать зашифрованное сообщение.
'''

def vigenere_cipher(message, keyword):
    encrypted_message = ""
    keyword_length = len(keyword)
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Преобразуем ключевое слово в числовой ключ
    key = [alphabet.index(char) for char in keyword]

    # Проходим по каждому символу в сообщении
    for i, char in enumerate(message):
        # Находим сдвиг для текущего символа
        ...
        # Шифруем символ с помощью сдвига
        ...

        else:
            # Если символ не буква, оставляем его без изменений
            ...

    return encrypted_message

# Пример использования
message = "hello, world!"
keyword = "python"
encrypted_message = vigenere_cipher(message, keyword)
print("Зашифрованное сообщение:", encrypted_message)

