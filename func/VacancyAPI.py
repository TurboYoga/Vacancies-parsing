from abc import ABC, abstractmethod
import requests
import os


SJ_KEY = os.getenv('SJ_API_KEY')


class AbstractVacancyAPI(ABC):

    @abstractmethod
    def get_request(self):
        '''Абстрактный класс для запросов API'''
        pass


class HH_API(AbstractVacancyAPI):

    def __init__(self, vacancy_name):
        self.url = "https://api.hh.ru/vacancies"
        self.params = {
            'text': vacancy_name,
            'search_field': 'name',
            'page': 0,
            'per_page': 100,
        }

    def get_request(self):

        return requests.get(self.url, self.params)




class SuperjobApi(AbstractVacancyAPI):

    def __init__(self, vacancy_name):
        self.url = 'https://api.superjob.ru/2.0/vacancies/'
        self.params = {
            'keywords': vacancy_name,
            'page': 1,
        }

    def get_request(self):
        headers = {"X-Api-App-Id":SJ_KEY}
        return requests.get(self.url, self.params, headers=headers)
