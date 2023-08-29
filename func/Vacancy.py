from func.VacancyAPI import HH_API


class Vacancy:
    def __init__(self, name, id, salary, requirements):
        self.name = name
        self.id = id
        self.salary = salary
        self.requirements = requirements


    def __ge__(self, other):
        self.other = other
        if not isinstance(other, int):
            raise TypeError ('Зарплата должна быть типа int')
        if self.salary > self.other:
            return f'Зарплата у {self.name} больше чем {self.other}'
        if self.salary < self.other:
            return f'Зарплата у {self.name} меньше чем {self.other}'
        if self.salary == self.other:
            return f'Зарплата у {self.name} и {self.other} равны'








