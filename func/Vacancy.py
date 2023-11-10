class Vacancy(object):
    def __init__(self, name, id, salary, requirements):
        self.name = name
        self.id = id
        self.salary = salary
        self.requirements = requirements

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value:
            self._salary = value     # ["from"] if value['from'] else value['to']
        else:
            self._salary = 0

    def __gt__(self, other):
        # Тут достаточно будет вернуть только True/False, так как по большей части метод нужен только для сортировки
        return self.salary > other.salary


    def __str__(self):
        # Нужен для вывода в интерфейс
        return (f"ID: {self.id}\n"
                f"Название вакансии: {self.name}\n"
                f"Зарплата: {self.salary}\n"
                f"Требования: {self.requirements}\n"
                f"=====")
