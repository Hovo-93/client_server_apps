import locale
import subprocess
import chardet

"""1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
 и также проверить тип и содержимое переменных."""

words = ['разработка', 'сокет', 'декоратор']

for word in words:
    print(type(word), word)

print('=' * 30)
ENC_STR_BYTES = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
]

for i in ENC_STR_BYTES:
    print(type(i), i)
# У меня вопрос почему когда исползуеться unicode_escape получаю <class 'bytes'>
# text = 'Привет!'.encode('unicode_escape')
# print(type(text))
# print(text)TODO

""" 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных."""
print('=' * 30)
words = [b'class', b'function', b'method']
for word in words:
    print(type(word), f'Длина соответствующих переменных-{len(word)}', '\n')
print('=' * 30)

"""3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе."""
word = b'attribute'
# word1 = b'класс'
# word3 = b'функция'
word4 = b'type'
"""word1 = b'класс'
            ^
 SyntaxError: bytes can only contain ASCII literal characters.
 На строки записанные на кириллице вылетает исключение"""
print('=' * 30)
"""4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
в байтовое и выполнить обратное преобразование (используя методы encode и decode)."""
words = ['разработка', 'администрирование', 'protocol', 'standard']
enc_str_byte = []
for word in words:
    enc_str_byte.append(word.encode('utf-8'))
    print(word.encode('utf-8'), type(word.encode('utf-8')), end='\n')
for i in enc_str_byte:
    print(i.decode('utf-8'))
print('=' * 30)

"""5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового
 в строковый тип на кириллице."""

ARGS = ['ping', 'yandex.ru']
ya_ping = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in ya_ping.stdout:
    result = chardet.detect(line)
    print(line.decode(result['encoding']))
print('=' * 30)

ARGS = ['ping', 'youtube.com']
ya_ping = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in ya_ping.stdout:
    result = chardet.detect(line)
    print(line.decode(result['encoding']))
print('=' * 30)
"""6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», 
«декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode 
и вывести его содержимое."""
F_N = open('test.txt', 'w', encoding='utf-8')
F_N.write('сетевое программирование,сокет,декоратор')
F_N.close()
F_N = locale.getpreferredencoding()
print(F_N, 'Проверка кодировки по умолчанию')
with open('test.txt', encoding='utf-8') as f_n:
    for line in f_n:
        print(line)
