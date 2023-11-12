from func.VacancyAPI import HH_API, SuperjobApi
from utils import get_vacancy_obj_list_hh, get_vacancy_obj_list_sj
from func.Vacancy_json import JsonSaver


def User():
    # Различные ответы можно добавить в список для обработки, например: 'хх.ру', 'sj.ru'
    platform = ['HH.ru', 'hh.ru', 'Superjob.ru', 'superjob.ru']
    platform_hh = ['HH.ru', 'hh.ru']
    platform_superjob = ['Superjob.ru', 'superjob.ru']\

    print('Привет \nМы готовы подобрать для вас вакансии \nВыбери платформу для поиска')

    while True:

        user_platform = input('HH.ru или Superjob.ru\n')
        if not user_platform in platform:
            print('У нас нет такой платформы \nВыбери из имеющихся')

        if user_platform in platform_hh:
            print('Отлично! \nВы выбрали HH.ru')

            while True:

                user_choice = input('''Введите название профессии: \n''')
                vacancy_name_keyword = user_choice

                # Инициализация объектов API
                hh_api = HH_API(vacancy_name_keyword)

                # Получение словаря с апи
                raw_vacancy_list_hh = hh_api.get_request().json()

                # Получение списка экземпляров класса вакансии
                obj_vacancy_list_hh = get_vacancy_obj_list_hh(raw_vacancy_list_hh)

                print('Создать файл с вакансиями?')

                user_file = input("Да/Нет\n")
                # Различные ответы можно добавить в список для обработки, например: 'No'
                answer_user = ['Да', 'да', 'Нет', 'нет']
                answer_user_yes = ['Да', 'да']
                answer_user_no = ['Нет', 'нет']

                if not user_file in answer_user:
                    print('Не верный ввод')

                elif user_file in answer_user:

                    if user_file in answer_user_yes:

                        # Вызов, метода, сохраняющего вакансии в json
                        JsonSaver.save_data_to_json_hh(obj_vacancy_list_hh)
                        print("Файл data_hh.json с вакансиями создан")

                        while True:
                            user_money = input('Введите минимальную желаемую зарплату для сортировки вакансий:\n')
                            if user_money.isdigit():
                                # Удаление вакансий из json
                                JsonSaver.remove_data_from_json_hh(user_money)
                                break
                            else:
                                print('Нужно ввести сумму цифрами, без пробелов, запятых и других знаков')
                        user_sorted = input('Хотите вывести в терминал вакансии?\nДа\Нет\n')
                        if user_sorted in answer_user_yes:
                            # Пример сортировки для интерфейса
                            for item in sorted(obj_vacancy_list_hh, reverse=True):
                                print(item)
                            break
                        else:
                            break
                    elif user_file in answer_user_no:
                        print('Ваши вакансии:\n')
                        for item in sorted(obj_vacancy_list_hh, reverse=True):
                            print(item)
                        print('До новых встреч')
                        break



        if user_platform in platform_superjob:
            print('Отлично! \nВы выбрали Superjob.ru')

            while True:

                user_choice = input('''Введите название профессии: \n''')
                vacancy_name_keyword = user_choice

                # Инициализация объектов API
                sj_api = SuperjobApi(vacancy_name_keyword)

                # Получение словаря с апи
                raw_vacancy_list_sj = sj_api.get_request().json()

                # Получение списка экземпляров класса вакансии
                obj_vacancy_list_sj = get_vacancy_obj_list_sj(raw_vacancy_list_sj)

                print('Создать файл с вакансиями?')

                user_file = input("Да/Нет\n")
                # Различные ответы можно добавить в список для обработки, например: 'No'
                answer_user = ['Да', 'да', 'Нет', 'нет']
                answer_user_yes = ['Да', 'да']
                answer_user_no = ['Нет', 'нет']

                if not user_file in answer_user:
                    print('Не верный ввод')

                elif user_file in answer_user:

                    if user_file in answer_user_yes:

                        # Вызов, метода, сохраняющего вакансии в json
                        JsonSaver.save_data_to_json_sj(obj_vacancy_list_sj)
                        print("Файл data_hh.json с вакансиями создан")

                        while True:
                            user_money = input('Введите минимальную желаемую зарплату для сортировки вакансий:\n')
                            if user_money.isdigit():
                                # Удаление вакансий из json
                                JsonSaver.remove_data_from_json_sj(user_money)
                                break
                            else:
                                print('Нужно ввести сумму цифрами, без пробелов, запятых и других знаков')
                        user_sorted = input('Хотите вывести в терминал вакансии?\nДа\Нет\n')
                        if user_sorted in answer_user_yes:
                            # Пример сортировки для интерфейса
                            for item in sorted(obj_vacancy_list_sj, reverse=True):
                                print(item)
                            break
                        else:
                            break
                    elif user_file in answer_user_no:
                        print('Ваши вакансии:\n')
                        for item in sorted(obj_vacancy_list_sj, reverse=True):
                            print(item)
                        print('До новых встреч')
                        break
        print('До новых встреч!')
        break
