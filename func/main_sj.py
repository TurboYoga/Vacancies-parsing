from func.VacancyAPI import SuperjobApi
from utils import get_vacancy_obj_list_sj
from func.Vacancy_json import JsonSaver


def Main_SJ():
    vacancy_name_keyword = 'python'

    # Инициализация объектов API
    sj_api = SuperjobApi(vacancy_name_keyword)

    # Получение словаря с апи
    raw_vacancy_list_sj = sj_api.get_request().json()

    # Получение списка экземпляров класса вакансии
    obj_vacancy_list_sj = get_vacancy_obj_list_sj(raw_vacancy_list_sj)

    # Вызов, метода, сохраняющего вакансии в json
    JsonSaver.save_data_to_json_sj(obj_vacancy_list_sj)

    # Удаление вакансий из json
    JsonSaver.remove_data_from_json_sj(100000)

    # Пример сортировки для интерфейса
    for item in sorted(obj_vacancy_list_sj, reverse=True):
        return item
