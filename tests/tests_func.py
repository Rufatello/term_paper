from utils import func
import json
import pytest
@pytest.fixture
def test_json_data():
    return [
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
  }
]


def test_load_json(test_json_data):
    with open('operations_1.json', 'w', encoding='utf-8') as test_file:
        json.dump(test_json_data, test_file)
    loaded_data = func.load_json('operations_1.json')
    assert loaded_data == test_json_data