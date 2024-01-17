'''
Требования

Последние 5 выполненных (EXECUTED) операций выведены на экран.
Операции разделены пустой строкой.
Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018).
Сверху списка находятся самые последние операции (по дате).
Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).
Номер счета замаскирован и не отображается целиком в формате  **XXXX
(видны только последние 4 цифры номера счета).

Файл модифицировать нельзя.
Все нестандартные записи обрабатывать программно.

Проект выложили на GitHub.
Есть файл .gitignore
Оформили файл README.md.
В проекте есть минимум 2 ветки, причем разработка ведется в `develop`, а стабильная версия на момент сдачи проекта лежит в ветке `main`.
Разработка проекта ведется в виртуальном окружении, в проекте есть информация о требованиях проекта (зависимостях).
К проекту написали тесты с покрытием не менее 80%.
Тесты написали на `pytest` или `unittest`.
Проект структурированный, читаемый, каждая функция — не более 50 строк.
Работа с файлом ведется через библиотеку json
'''

from functions import *

data = open_file() # Все операции
filter_data = filter_list_only_executed(data) #только EXECUTED
# print(filter_data)
sorted_data = sorted(filter_data, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)[:5] #отсортировываем по дате, reverse=...
dates = modify_date(sorted_data)
card_number = modify_bill(sorted_data)
amount_number = get_format_check(sorted_data)

for operation in range(len(sorted_data)):
    print(f"{dates[operation]} {sorted_data[operation]['description']}")
    print(f"{card_number[operation]} -> {amount_number[operation]}")
    print(f"{sorted_data[operation]['operationAmount']['amount']} {sorted_data[operation]['operationAmount']['currency']['name']}\n")






















# from functions import *
#
# data = open_file() # Все операции
# filter_data = filter_list_only_executed(data) #только EXECUTED
# # print(filter_data)
# sorted_data = filter_data.sort(filter_data, key=lambda x: x['date'], reverse=True)[:5] #отсортировываем по дате, reverse=...
#
#
#
# for trans in data:
#     formatted = format_operation(trans)
#     print(formatted)

