from func.VacancyAPI import HH_API, SuperjobApi
from utils import get_vacancy_obj_list_hh, get_vacancy_obj_list_sj
from func.Vacancy_json import JsonSaver


def main():
    vacancy_name_keyword = 'python'

    # Инициализация объектов API
    hh_api = HH_API(vacancy_name_keyword)
    sj_api = SuperjobApi(vacancy_name_keyword)

    # Получение словаря с апи
    raw_vacancy_list_hh = hh_api.get_request().json()
    raw_vacancy_list_sj = sj_api.get_request().json()

    # Получение списка экземпляров класса вакансии
    obj_vacancy_list_hh = get_vacancy_obj_list_hh(raw_vacancy_list_hh)
    obj_vacancy_list_sj = get_vacancy_obj_list_sj(raw_vacancy_list_sj)

    # Вызов, метода, сохраняющего вакансии в json
    JsonSaver.save_data_to_json_hh(obj_vacancy_list_hh)
    JsonSaver.save_data_to_json_sj(obj_vacancy_list_sj)

    # Удаление вакансий из json
    JsonSaver.remove_data_from_json_hh(100000)
    JsonSaver.remove_data_from_json_sj(100000)

    # Пример сортировки для интерфейса
    for item in sorted(obj_vacancy_list_hh, reverse=True):
        print(item)

    print('=============================================')

    for item in sorted(obj_vacancy_list_sj, reverse=True):
        print(item)

if __name__ == '__main__':
    main()
