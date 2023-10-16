import requests
import json
import time


def get_vacancies_data(emp_ids: list):
    answer_hh = {'items': []}
    for emp_id in emp_ids:
        params = {
            'employer_id': emp_id,  # ID
            'area': 113,  # Поиск в зоне
            'page': 0,  # Номер страницы
            'per_page': 50  # Кол-во вакансий на 1 странице
        }
        req = requests.get('https://api.hh.ru/vacancies', params)
        data = req.content.decode()
        req.close()
        hh_json = json.loads(data)
        time.sleep(1)
        answer_hh['items'].extend(hh_json['items'])
    return answer_hh


def get_emp_data(emp_ids: list):
    answer_hh_emp = []
    for emp_id in emp_ids:
        params = {
            'employer_id': emp_id,  # ID
            'area': 113,  # Поиск в зоне
            'page': 0,  # Номер страницы
            'per_page': 1  # Кол-во вакансий на 1 странице
        }
        req = requests.get('https://api.hh.ru/vacancies', params)
        data = req.content.decode()
        req.close()
        hh_json = json.loads(data)
        time.sleep(0.2)
        answer_hh_emp.append(hh_json)
    return answer_hh_emp
