class MixinAPI:
    """
    Класс миксин, для отправки GET запроса по API.
    """
    url: str = ''
    headers: dict = {}
    params: dict = {}
    field_the_number_of_lines: str = ''
    field_items: str = ''

    def get_vacancies(self, vacancy_name: str) -> List[dict]:
        """
        Отправляет GET-запрос по API и получает список вакансий.
        :param vacancy_name: Название вакансии.
        :return: Список словарей с информацией о вакансиях.
        """
        logger.info("Отправка GET-запроса к API сайтов.")
        list_vacancies: List[dict] = []
        self.params['page'] = 0
        while True:
            try:
                response = requests.get(self.url, headers=self.headers, params=self.params)
                response.raise_for_status()
                vacancy = response.json()
            except requests.exceptions.RequestException as e:
                raise HTTPError(f'Ошибка при отправке запроса: {e}')
            except ValueError as e:
                raise HTTPError(f'Ошибка при обработке ответа: {e}')

            count_vacancy = vacancy[self.field_the_number_of_lines]
            total_pages = (count_vacancy + 99) // 100

            list_vacancies += vacancy[self.field_items]
            self.params['page'] += 1

            if self.params['page'] >= total_pages:
                break

        return list_vacancies




class HeadHunterAPI(MixinAPI, AbstractVacancyAPI):
    """
    Класс для работы с API сайта HeadHunter.
    Наследуется от MixinAPI и AbstractVacancyAPI.
    """
    url: str = 'https://api.hh.ru/vacancies'
    params: dict = {}
    field_the_number_of_lines: str = 'found'
    field_items: str = 'items'
    page: int = 0

    def get_vacancies(self, vacancy_name: str) -> List[dict]:
        self.params = {
            'text': vacancy_name,
            'search_field': 'name',
            'page': self.page,
            'per_page': 100,
        }
        logger.info("Получены вакансии из HeadHunter.")
        return super().get_vacancies(vacancy_name)

#########################################################################


class MixinAPI:
    """
        Класс миксин, для отправки GET запроса по API.
    """
    url: str = ''
    headers: dict = {}
    params: dict = {}
    field_the_number_of_lines: str = ''
    field_items: str = ''

###############################################################################

from pprint import pprint

import requests

params = {
    'text': "python",
    'search_field': 'name',
    'page': 1,
    'per_page': 100,
}

url: str = 'https://api.hh.ru/vacancies'

headers: dict = {}

result = requests.get(url, headers=headers, params=params)

pprint(result.json())


###########################################################################


def connect_to_API(self, start_page=0, per_page=MAX_COUNT_VACANCY_FOR_ONE_API_PAGE):
    """
    we need to create request such as 'https://api.hh.ru/vacancies?text=java&area=1'
    :return:
    """
    url = MAIN_REQUEST_FOR_HH
    url += f"?enable_snippets=true&text={self.params['text']}&area={self.params['area']}"
    url_with_pages = url + f"&page={start_page}&per_page={per_page}"
    print(url_with_pages)  # need chane to logger
    headers = {"User-Agent": MY_APP_NAME}
    response = requests.get(url_with_pages, headers=headers)
    if response.status_code == 200:
        self.content = json.loads(response.text)
        self.content_inside.extend(self.content.get("items"))
    print("HH API response is:", response)  # need chane to logger



###################################################################################

    def get_parsed_data(self):
        """ parse data which received from API or raw-file for HedHunter format"""
        for item in self.content_inside:
            vacancy = Vacancy()
            try:
                vacancy.title = item["name"]
                vacancy.url = item.get("alternate_url")
                if item.get("salary"):
                    vacancy.salary_min = item["salary"].get("from") if item["salary"].get("from") else 0
                    vacancy.salary_max = item["salary"].get("to") if item["salary"].get("to") else 0
                vacancy.description = item["snippet"].get("requirement")
            except Exception as err:
                print("bad data in item", err)
            self.vacancy_list.append(vacancy)
        return self.vacancy_list


########################################################################################

    def connect_to_API(self, start_page=5, count=100):
        """
        we need to create request such as 'https://api.superjob.ru/2.0/vacancies/?t=4&count=100'
        :return:
        """
        url = MAIN_REQUEST_FOR_SJ
        url += f"/?&keyword={self.params['text']}&t={self.params['area']}"
        url_with_pages = url + f"&page={start_page}&count={count}"
        print(url_with_pages)  # need chane to logger
        headers = {"X-Api-App-Id": SUPER_JOB_KEY}
        response = requests.get(url_with_pages, headers=headers)
        if response.status_code == 200:
            self.content = json.loads(response.text)
            self.content_inside.extend(self.content.get("objects"))
        print("SurerJob API response is:", response)  # need chane to logger


##########################################################################################


 def get_json(self):
        """returns object data in json format"""
        return {"title": self.title,
                "description": self.description,
                "salary_min": self.salary_min,
                "salary_max": self.salary_max,
                "url": self.url
                }