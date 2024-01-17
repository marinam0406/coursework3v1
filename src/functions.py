import os
import json
from datetime import datetime

from config import ROOT_DIR


OPERATION = os.path.join(ROOT_DIR, 'operations.json')


def open_file():
    """функция открытия файла, возвращает открытый файл"""
    with open(OPERATION, encoding='UTF8') as file:
        file_name = json.load(file)
    return file_name  # открытый файл


def filter_list_only_executed(data):
    """формирует новый список, в котором только EXECUTED операции"""
    # {}
    new_data = []
    for item in data:
        if item.get('state') == 'EXECUTED': # {} .get()
            new_data.append(item)
    return new_data


def modify_date(format_date):  # дата строкой
    """
    форматирует дату
    :param data:"2019-08-26T10:50:58.294041"
    :return:"26.08.2019"
    """
    date_list = []
    for item_data in format_date:
        date = datetime.strptime(item_data['date'], "%Y-%m-%dT%H:%M:%S.%f")
        date_format = f"{date:%d.%m.%Y}"
        date_list.append(date_format)
    return date_list  # "26.08.2019"


def modify_bill(bill):  # отправитель или получатель строкой
    """
    форматирует реквизиты отправителя или получателя
    :param bill:"Maestro 1596837868705199"
    :return:"Maestro 1596 83** **** 5199"
    """
    format_bill = []
    for item in bill:
        if item["description"] == "Открытие вклада":
            item['from'] = f"Счёт клиента: **{item['to'][-4:]}"
        elif item["from"][0:4] == "Счет":
            item['from'] = f"Счёт: **{item['from'][-4:]}"
        else:
            item['from'] = item['from'][0:-12] + ' ' + item['from'][-12:-10] + '** **** ' + item['from'][-4:]
        format_bill.append(item['from'])
    return format_bill  # "Maestro 1596 83** **** 5199"

def get_format_check(checks_to):
    """
    Выводит счет в замаскированом формате последние 4 цифры '**счет'
    """
    list_check = []
    for item in checks_to:
        if item["to"][0:4] == "Счет":
            item['to'] = f"Счёт: **{item['to'][-4:]}"
        else:
            item['to'] = item['to'][0:-12] + ' ' + item['to'][-12:-10] + '** **** ' + item['to'][-4:]
        list_check.append(item['to'])
    return list_check





















# def silens_card(card_from):
#     card_silens = '{} {}** **** {}'.format(card_from[:-12], card_from[-10:-8], card_from[-4:])
#     return silens_card
#
#
# def silens_account(account_to):
#     account_silens = 'Счет **{}'.format(account_to[-4:])
#     return account_silens
#
# def format_operation(transaction):
#     transaction['data'] = modify_date(transaction['data'])
#     # обработка, если есть или нет ключа from ""
#     transaction['from'] = modify_bill(transaction['from'])
#     transaction['to'] = modify_bill(transaction['to'])
#     # составить строку для принта
#     return (f"{transaction['data']} Перевод организации{transaction['from']}\n -> Счет {transaction['to']}\n "
#             f"{filter_data['operationAmount']['currency']['name']}")