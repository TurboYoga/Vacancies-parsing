import json
from abc import ABC
from utils import DATA_JSON_PATH_HH, DATA_JSON_PATH_SJ

class JsonSaver(ABC):

    @classmethod
    def save_data_to_json_hh(cls, data: list):
        # Получение значений всех свойств экземпляров
        vacancy_properties_dict = []
        for item in data:
            if isinstance(item, dict):
                vacancy_properties_dict.append(item)
            else: # Vacancy
                vacancy_properties_dict.append(item.__dict__)
        # vacancy_properties_dict = [item.__dict__ for item in data]

        # Сохранение всех вакансий в файл
        with open('data_hh.json', 'w', encoding='utf-8') as file:
            json.dump(vacancy_properties_dict, file, indent=4, ensure_ascii=False)

    @classmethod
    def save_data_to_json_sj(cls, data: list):
        # Получение значений всех свойств экземпляров
        vacancy_properties_dict = []
        for item in data:
            if isinstance(item, dict):
                vacancy_properties_dict.append(item)
            else:  # Vacancy
                vacancy_properties_dict.append(item.__dict__)
        # vacancy_properties_dict = [item.__dict__ for item in data]

        # Сохранение всех вакансий в файл
        with open('data_sj.json', 'w', encoding='utf-8') as file:
            json.dump(vacancy_properties_dict, file, indent=4, ensure_ascii=False)

    @classmethod
    def select_data_from_json_hh(cls):
        # Метод, забирающий вакансии
        with open(DATA_JSON_PATH_HH, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    @classmethod
    def select_data_from_json_sj(cls):
        # Метод, забирающий вакансии
        with open(DATA_JSON_PATH_SJ, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data


    @classmethod
    def remove_data_from_json_hh(cls, min_salary=100000):
        # Метод, удаляющий вакансии hh
        data = cls.select_data_from_json_hh()
        data = [item for item in data if item['_salary'] > int(min_salary)]
        cls.save_data_to_json_hh(data)

    @classmethod
    def remove_data_from_json_sj(cls, min_salary=100000):
        # Метод, удаляющий вакансии sj
        data = cls.select_data_from_json_sj()
        data = [item for item in data if item['_salary'] > int(min_salary)]
        cls.save_data_to_json_sj(data)
