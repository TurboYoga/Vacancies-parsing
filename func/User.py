


class User:

    platform = ['HH.ru', 'hh.ru', 'Superjob.ru', 'superjob.ru']
    platform_hh = ['HH.ru', 'hh.ru']
    platform_superjob = ['Superjob.ru', 'superjob.ru']
    print('Привет \nМы готовы подобрать для вас вакансию \nВыбери платформу для поиска')
    while True:
        user_platform = input('HH.ru или Superjob.ru \n')
        if not user_platform in platform:
            print('У нас нет такой платформы \nВыбери из имеющихся')

        if user_platform in platform_hh:
            print('Отлично! \nВы выбрали HH.ru \nДавай теперь выберем что именно вам нужно:')

            while True:
                user_choice = input('''
                            Выберите цифру:
                            1) Топ 10 вакансий по заработной плате
                            2) Поиск по ключевым словам
                            3) Список востребованных вакансий
                            ''')
                categories = ['1', '2', '3']
                if not user_choice in categories:
                    print('Такой категории нет, выберите другую')
                if user_choice == categories[0]:
                    print(1)
                    break
                elif user_choice == categories[1]:
                    print(2)
                    break
                elif user_choice == categories[2]:
                    print(3)
                    break
            break

        if user_platform in platform_superjob:
            print('Отлично! \nВы выбрали Superjob.ru \nДавай теперь выберем что именно вам нужно:')
            user_choice = input('''
                        Выберите цифру:
                        1) Топ 10 вакансий по заработной плате
                        2) Поиск по ключевым словам
                        3) Список востребованных вакансий
                        ''')
            break