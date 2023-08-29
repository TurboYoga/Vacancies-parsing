from abc import ABC
import json
from pprint import pprint

from func.VacancyAPI import HH_API


class Work_json(ABC):

    def add_json(self):
        with open('Vacancy_json.txt') as file:
          print(file)


