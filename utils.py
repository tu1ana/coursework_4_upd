from api_class import HeadHunterAPI, SuperJobAPI
from job_class import Job
from record_class import SaveToJSON


def user_interaction():
    while True:
        username = input('Здравствуйте! Введите Ваше имя: ')
        platform = input(f'{username}, выберите платформу: 1 - HeadHunter, 2 - SuperJob, 3 - Выход\n')
        if platform == '1':
            hh_query = input('Введите название интересующей вакансии или ключевое слово:\n')
            hh_api = HeadHunterAPI()
            hh_data = hh_api.get_vacancies(hh_query)
            if not hh_data:
                print('По Вашему запросу ничего не найдено')
            else:
                hh_filtered_data = [item for item in hh_data if item.get('salary') is not None]
                hh_sorted_data = sorted(hh_filtered_data, key=lambda x: x['salary'] if x['salary'] else 'Не указано', reverse=True)
                hh_top = int(input('Введите число для вывода топ-N вакансий: '))
                hh_top_data = hh_sorted_data[:hh_top]
                job_list = []
                for item in hh_top_data:
                    job = Job(item['title'], item['salary'], item['description'], item['url'])
                    job_list.append(job)

                for job in job_list:
                    print(
                        f'Должность: {job.title}\n'
                        f'Зарплата: {job.salary}\n'
                        f'Описание: {job.description}\n'
                        f'Ссылка: {job.url}\n'
                    )
                record_entry = input(f'{username}, вы хотите сохранить данные? (y / n)\n')
                if record_entry.lower() == 'y':
                    save_to_json = SaveToJSON()
                    save_to_json.add_jobs_to_file(job.json_entry())
                else:
                    return
        elif platform == '2':
            superjob_query = input('Введите название интересующей вакансии:\n')
            superjob_api = SuperJobAPI()
            superjob_data = superjob_api.get_vacancies(superjob_query)

            if not superjob_data:
                print('По Вашему запросу ничего не найдено')
            else:
                superjob_filtered_data = [item for item in superjob_data if item.get('salary') is not None]
                superjob_sorted_data = sorted(superjob_filtered_data,
                                              key=lambda x: x['salary'] if x['salary'] else 'Не указано',
                                              reverse=True)
                superjob_top = int(input('Введите число для вывода топ-N вакансий: '))
                superjob_top_data = superjob_sorted_data[:superjob_top]
                job_list = []
                for item in superjob_top_data:
                    job = Job(item['title'], item['salary'], item['description'], item['url'])
                    job_list.append(job)

                for job in job_list:
                    print(
                        f'Должность: {job.title}\n'
                        f'Зарплата: {job.salary}\n'
                        f'Описание: {job.description}\n'
                        f'Ссылка: {job.url}\n'
                    )
                record_entry = input(f'{username}, вы хотите сохранить данные? (y / n)\n')
                if record_entry.lower() == 'y':
                    save_to_json = SaveToJSON()
                    save_to_json.add_jobs_to_file(job.json_entry())
                else:
                    return

        elif platform == '3':
            print('Спасибо, хорошего дня!')
            break
        else:
            print('Что-то пошло не так, попробуйте ещё раз')


user_interaction()
