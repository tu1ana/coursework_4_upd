import json
from abc import ABC, abstractmethod


class RecordData(ABC):

    @abstractmethod
    def add_jobs_to_file(self, keyword):
        pass

    @abstractmethod
    def get_jobs_from_file_by_keyword(self, keyword):
        pass


class SaveToJSON(RecordData):

    def __init__(self):
        self.filename = 'headhunter.json'

    def add_jobs_to_file(self, job: dict):
        with open(self.filename, 'a', encoding='utf-8') as file:
            json.dump(job, file, ensure_ascii=False, indent=4, separators=(', ', ': '))
            file.write('\n')

    def get_jobs_from_file_by_keyword(self, keyword: str):
        filtered_job_list = []
        with open(self.filename, encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                if keyword in item['title']:
                    filtered_job_list.append(item)
        return filtered_job_list
