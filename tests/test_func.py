from pathlib import Path

from utils.func import load_json, date_last

TESTING_DATA = Path(__file__).resolve().parent / "operations_1.json"


def test_load_json():

    expected_data = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-09-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
]

    assert load_json(TESTING_DATA) == expected_data


def test_date_last():
    test_data = [
        {
            "id": 1,
            "date": "2023-09-01T10:00:00",
        },
        {
            "id": 2,
            "date": "2023-09-02T10:00:00",
        },
        {
            "id": 3,
            "date": "2023-09-03T10:00:00",
        }
    ]

    expected_result = [
        {
            "id": 3,
            "date": "2023-09-03T10:00:00",
        },
        {
            "id": 2,
            "date": "2023-09-02T10:00:00",
        },
        {
            "id": 1,
            "date": "2023-09-01T10:00:00",
        }
    ]
    sorted_data = date_last(test_data)
    assert sorted_data == expected_result