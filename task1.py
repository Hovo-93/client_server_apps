"""1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных
данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:"""

import csv
from pathlib import Path

pathlist = Path('info_data').rglob('*.txt')


def get_data(path_list):
    os_name_list = []
    os_type_list = []
    os_code_list = []
    os_prod_list = []
    big_data = []
    finally_data = []
    main_data = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    os_prod = 'Изготовитель системы'
    os_name = 'Название ОС:'
    os_code = 'Код продукта'
    os_type = 'Тип системы'
    for path in path_list:
        with open(path) as file:
            reader = csv.reader(file)
            for i in reader:
                for j in i:
                    if os_name in j:
                        os_name_list.append(j[34:])
                    if os_code in j:
                        os_code_list.append((j[34:]))
                    if os_type in j:
                        os_type_list.append(j[34:])
                    if os_prod in j:
                        os_prod_list.append(j[34:])
    big_data.append(os_prod_list)  # ['LENOVO', 'ACER', 'DELL']
    big_data.append(os_name_list)
    big_data.append(os_code_list)
    big_data.append(os_type_list)

    correct_date1 = []  # ['LENOVO', 'Microsoft Windows 7 Профессиональная ', '00971-OEM-1982661-00231', 'x64-based PC']
    correct_date2 = []
    correct_date3 = []
    for i in big_data:
        correct_date1.append(i[0])
        correct_date2.append(i[1])
        correct_date3.append(i[2])
    print(correct_date1)

    finally_data.append(main_data)
    finally_data.append(correct_date1)
    finally_data.append(correct_date2)
    finally_data.append(correct_date3)
    return finally_data


DATA = get_data(pathlist)
print(DATA)


def write_to_csv(data):
    with open('kp_data_write_1.csv', 'w', encoding='utf-8') as f_n:
        F_N_WRITER = csv.writer(f_n)
        for row in data:
            F_N_WRITER.writerow(row)


write_to_csv(DATA)
# Не изучал тему рег-выражения поэтому решил так)
