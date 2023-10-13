import json
import time

import requests

if __name__ == '__main__':

    company_ids = [64174, 56132, 75112]
    for ids in company_ids:
        params = {
            'employer_id': ids,  # ID 2ГИС
            'area': 113,  # Поиск в зоне
            'page': 0,  # Номер страницы
            'per_page': 10  # Кол-во вакансий на 1 странице
        }
        req = requests.get('https://api.hh.ru/vacancies', params)
        data = req.content.decode()
        req.close()
        hh_json = json.loads(data)
        time.sleep(5)
        print(hh_json)

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

