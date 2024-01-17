from src.functions import *


def test_modify_date():
    assert modify_date([{"date": "2019-08-26T10:50:58.294041"}]) == ['26.08.2019']


def test_modify_bill():
    assert modify_bill([{
    "id": 484201274,
    "state": "EXECUTED",
    "date": "2019-04-11T23:10:21.514616",
    "operationAmount": {
      "amount": "62621.51",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "МИР 8193813157568899",
    "to": "МИР 9425591958944146"
  }]) == ['МИР 8193 81** **** 8899']


def test_get_format_check():
    assert (get_format_check([{
    "id": 484201274,
    "state": "EXECUTED",
    "date": "2019-04-11T23:10:21.514616",
    "operationAmount": {
      "amount": "62621.51",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "МИР 8193813157568899",
    "to": "МИР 9425591958944146"
  }]) == ['МИР 9425 59** **** 4146'])
    assert (get_format_check([{
    "id": 547682597,
    "state": "EXECUTED",
    "date": "2018-12-29T21:45:18.495053",
    "operationAmount": {
      "amount": "66263.93",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 77977573135347241529",
    "to": "Счет 33062909508148771891"
  }]) == ['Счёт: **1891'])
