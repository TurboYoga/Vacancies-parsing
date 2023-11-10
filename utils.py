from func.Vacancy import Vacancy
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATA_JSON_PATH_HH = Path.joinpath(ROOT, 'data_hh.json')
DATA_JSON_PATH_SJ = Path.joinpath(ROOT, 'data_sj.json')


def hh_salary_convert(salary):
    if salary:
        if salary['from']:
            salary_convert = salary['from']
            return salary_convert
        else:
            salary_convert = salary['to']
            return salary_convert
    else:
        salary_convert = 0
        return salary_convert


def get_vacancy_obj_list_hh(vacancies_from_api):
    vacancies = []
    for vacancy in vacancies_from_api['items']:
        vacancies.append(
            Vacancy(
                name=vacancy['name'],
                id=vacancy['id'],
                salary=hh_salary_convert(vacancy['salary']),
                requirements=vacancy['snippet']['requirement']
            )
        )
    return vacancies


def get_vacancy_obj_list_sj(vacancies_from_api):
    vacancies = []
    for vacancy in vacancies_from_api['objects']:
        vacancies.append(
            Vacancy(
                name=vacancy['profession'],
                id=vacancy['id'],
                salary=vacancy['payment_from'],
                requirements=vacancy['experience']['title']
            )
        )
    return vacancies
