import json


def load_json(a):
    with open(a, encoding="utf-8") as f:
        file_json_1 = json.load(f)
        return file_json_1


file_json = load_json('operations.json')


def date_last():
    '''функция сортирует все значения по дате от наименьшего к наибольшему'''
    sorted_data_1 = sorted(file_json, key=lambda x: x.get('date'), reverse=True)
    return sorted_data_1


sorted_data = date_last()


# создаем пустой список для записи первых 5 значений
five_str_load = []


def load_str():
    '''функция записи последних элементов со статусом "EXECUTED",
    если статус ==EXECUTED, то переменная счетчик увеличивается на 1
    и происходит запись в словарь, как только переменная счетчик будет равна 5, цикл автоматом вырубается'''
    count = 0

    for state_status in sorted_data:
        state = state_status.get('state', '')

        if state == 'EXECUTED':
            five_str_load.append(state_status)
            count += 1

        if count == 5:
            break
    return five_str_load


five_list = load_str()

# создаем 2 списка для записи в них наименования банка и наименоваие счета
numb_bank = [] # имя банка
numb_kart = [] # имя счета


def function_five_load(an):
    '''функция извлекает все статусы из списка и разделяет
    далее через сплит разделяет по пробелу все значения и записывает их в новые списки'''

    for r in an:
        from_1 = r.get('from', '')
        w = from_1.split(' ')

        numb_bank.append(' '.join(w[:-1]))
        numb_kart.append(''.join(w[-1]))
    return numb_bank, numb_kart


numb_bank, numb_kart = function_five_load(five_list)

# создаем пустой список, чтобы добавить звездочки, вместе символов

replay_numb_kart = []


def stars_numb(q):
    '''функция для преобразования некоторых чисел в звездочки
    и записи их в новый список'''
    for o in q:
        stars = len(o) - 10

        replay_numb_kart.append(o[:6] + "*" * stars + o[-4:])
    return replay_numb_kart


numb_kart = stars_numb(numb_kart)

result_strings = []

for string in numb_kart:
    for i in range(0, len(string), 4):
        formatted_string = ' '.join([string[i:i + 4] for i in range(0, len(string), 4)])
        result_strings.append(formatted_string)

#result_list()



for list_bank, s, list_numb in zip(numb_bank, five_str_load, result_strings):
    data_operation = s['date']
    description = s['description']
    name = s['operationAmount']['currency']['name']
    summ_operation = s['operationAmount']['amount']
    date = s['date']
    to = s['to'][:-14].replace('Счет ', '')
    print(f'{date[:10].replace("-", ".")} {description}\n'
          f'{list_bank} {list_numb} -> Счет **{to[2:]}\n'
          f'{summ_operation} {name}\n')
