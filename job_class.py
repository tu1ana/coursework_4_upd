class Job:

    def __init__(self, title, salary, description, url):
        self.title = title
        self.salary = salary
        self.description = description
        self.url = url

    def __str__(self):
        return f'Должность: {self.title}\nЗарплата: {self.salary}\n' \
               f'Описание: {self.description}\nСсылка на вакансию: {self.url}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.title}, {str(self.salary)}, {self.description}, {self.url})'

    def __gt__(self, other):
        return self.salary > other.salary

    def json_entry(self):
        return {
            'title': self.title,
            'salary': self.salary,
            'description': self.description,
            'url': self.url
        }
