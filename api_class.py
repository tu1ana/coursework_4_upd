import os
from abc import ABC, abstractmethod

import requests


class API(ABC):
    @abstractmethod
    def get_vacancies(self, query: str):
        pass


class HeadHunterAPI(API):
    def get_vacancies(self, query: str):
        params = {
            'text': query,
            'page': 0,
            'per_page': 100
        }
        response = requests.get('https://api.hh.ru/vacancies', params=params)
        data = response.json()
        job_list = []
        job_data = data['items']
        for job in job_data:
            title = job['name']

            if job['salary'] is None:
                salary = f'Зарплата не указана'
            elif job['salary'] is not None and job['salary']['to'] is not None:
                salary = f'Верхний порог зарплаты - {job["salary"]["to"]}'
            elif job['salary']['to'] is None and job['salary']['from'] is not None:
                salary = f'Нижний порог зарплаты - {job["salary"]["from"]}'
            else:
                salary = f'{job["salary"]["from"]} - {job["salary"]["to"]}'

            description = job['snippet']['requirement'] if job['snippet']['requirement'] is not None else \
            job['snippet']['responsibility']
            url = job['alternate_url']
            job_list.append({'title': title, 'salary': salary, 'description': description, 'url': url})
        return job_list


class SuperJobAPI(API):

    def get_vacancies(self, query: str):
        api_key = os.getenv('SUPERJOB_API_KEY')
        headers = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': api_key,
            'Authorization': 'Bearer r.000000010000001.example.access_token',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        params = {
            'keyword': query,
            'page': 0,
            'count': 100
        }
        response = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params=params)
        data = response.json()

        job_list = []
        job_data = data['objects']
        for job in job_data:
            title = job['profession']

            if job['payment_from'] is None and job['payment_to'] is None:
                salary = 'Зарплата не указана'
            elif job['payment_from'] is None and job['payment_to'] is not None:
                f'Верхний порог зарплаты - {job["payment_to"]}'
            elif job['payment_from'] is not None and job['payment_to'] is None:
                f'Нижний порог зарплаты - {job["payment_from"]}'
            else:
                salary = f'{job["payment_from"]} - {job["payment_to"]}'
            # salary = job['payment_from'] if job['payment_from'] is not None else 'Зарплата не указана'
            description = job['candidat']
            url = job['link']
            job_list.append({'title': title, 'salary': salary, 'description': description, 'url': url})
        return job_list
