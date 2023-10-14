import requests
import json
import time


def get_vacancies(emp_ids: list):
    answer_hh = []
    for emp_id in emp_ids:
        params = {
            'employer_id': emp_id,  # ID
            'area': 113,  # Поиск в зоне
            'page': 0,  # Номер страницы
            'per_page': 30  # Кол-во вакансий на 1 странице
        }
        req = requests.get('https://api.hh.ru/vacancies', params)
        data = req.content.decode()
        req.close()
        hh_json = json.loads(data)
        time.sleep(1)
        answer_hh.append(hh_json)
    return answer_hh
