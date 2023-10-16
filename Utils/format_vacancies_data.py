
def format_vacancies_data(answer_data_vac, answer_data_emp):
    """Функция для форматирования полученных данных в более наглядный вид"""
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
