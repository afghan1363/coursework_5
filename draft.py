import requests
import json
import time

from Utils.get_vacancies_data import get_vacancies

if __name__ == '__main__':

    class TreatmentVacancies:
        company_ids = [64174, 1740, 4023, 2324020, 328931, 2016792, 4219, 6093, 39305, 1439]

        def __init__(self):
            self.vacancies_data = []
            self.employers_data = []

        def get_vacancies_data(self):
            answer_hh = {'items': []}
            for emp_id in self.company_ids:
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

        def get_emp_data(self):
            answer_hh_emp = []
            for emp_id in self.company_ids:
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

        def format_vacancies_data(answer_data_vac, answer_data_emp):
            vacancy_data = {'employers': [],
                            'vacancies': []}
            for data in answer_data_emp:
                vacancy_data['employers'].append({'employer_id': data['items'][0]['employer']['id'],
                                                  'employer_name': data['items'][0]['employer']['name'],
                                                  'employer_url': data['items'][0]['employer']['alternate_url'],
                                                  'vacancy_count': data['found']})
            for data in answer_data_vac['items']:
                if not data['salary']:
                    data['salary'] = {}
                if not data['snippet']['responsibility']:
                    data['snippet']['responsibility'] = data['name']
                vacancy_data['vacancies'].append({'vacancy_id': data['id'],
                                                  'employer_id': data['employer']['id'],
                                                  'vacancy_title': data['name'],
                                                  'description': data['snippet']['responsibility'],
                                                  'salary_from': data['salary'].get('from'),
                                                  'salary_to': data['salary'].get('to'),
                                                  'city': data['area']['name'],
                                                  'vacancy_url': data['alternate_url']})
            return vacancy_data

    # for ids in company_ids[:3]:
    #     params = {
    #         'employer_id': ids,  # ID 2ГИС
    #         'area': 113,  # Поиск в зоне
    #         'page': 0,  # Номер страницы
    #         'per_page': 10  # Кол-во вакансий на 1 странице
    #     }
    #     req = requests.get('https://api.hh.ru/vacancies', params)
    #     data = req.content.decode()
    #     req.close()
    #     hh_json = json.loads(data)
    #     time.sleep(5)
    #     print(hh_json)

    # def getEmployers():
    #     req = requests.get('https://api.hh.ru/employers')
    #     data = req.content.decode()
    #     req.close()
    #     count_of_employers = json.loads(data)['found']
    #     employers = []
    #     i = 0
    #     j = count_of_employers
    #     while i < j:
    #         req = requests.get('https://api.hh.ru/employers/' + str(i + 1))
    #         data = req.content.decode()
    #         req.close()
    #         jsObj = json.loads(data)
    #         try:
    #             employers.append([jsObj['id'], jsObj['name']])
    #             i += 1
    #             print([jsObj['id'], jsObj['name']])
    #         except:
    #             i += 1
    #             j += 1
    #         if i % 200 == 0:
    #             time.sleep(0.2)
    #     return employers
    #
    #
    # employers = getEmployers()
    # def add_f(n):
    #     n.append('a')
    #
    # a = ['3']
    # add_f(a)
    #
    # print(a)
    # a = {}
    # a['a'] = 1
    # a['b'] = 2
    # print(f"a - {a}")
    # b = a
    # a = {}
    # print(b)
    # print(a)
