"""2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией
о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для этого:
a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item),
количество (quantity), цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных
в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
b. Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра."""

import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='utf-8') as f_n:
        OBJ = json.load(f_n)

        with open('json_data_write_2.json', 'w', encoding='utf-8') as file:
            OBJ_LIST = OBJ['orders']
            OBJ_DICT = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
            OBJ_LIST.append(OBJ_DICT)
            json.dump(OBJ, file, indent=4)


write_order_to_json('scanner', 10, 100, 'I.I', '22.22.22')
