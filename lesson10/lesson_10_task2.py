import json
import pickle
import os
from pathlib import Path

class Work_whith_files:
    @staticmethod
    def json2pickle(Path) -> None:
        for file in path.iterdir():
            if file.is_file() and file.suffix == '.json':
                with open(file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                with open(f'{file.stem}.pickle', 'wb') as f:
                    pickle.dump(data, f)

    @staticmethod
    def save_info_users():
        dict_1 = {str(i): {} for i in range(1,8)}
        set_1 = set()
        if os.path.isfile('users.json'):
            print('Фаил существует')
            with open('users.json', 'r', encoding='UTF-8') as f:
                dict_1 = json.load(f)
                for k, v in dict_1.items():
                    for k_1 in v:
                        set_1.add(k_1)
        while True:
            level = input('Введите уровень доступа ')
            id = input('Введите идентификатор ')
            name = input('Введите имя ')
            if int(level) in range(1, 8) and name and id not in set_1:
                dict_1[level][id] = name
                set_1.add(id)
                with open('users.json', 'w', encoding='UTF-8') as f:
                    json.dump(dict_1, f, ensure_ascii=False, indent=2)
            else:
                print('Введите корректные данные')

    @staticmethod
    def create_json_from_result(file):
        dict_1 = {}
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                name, number = line.split()
                dict_1[name.capitalize()] = float(number)
        with open('results.json', 'w', encoding='utf-8') as f:
            json.dump(dict_1, f, ensure_ascii=False, indent=2)