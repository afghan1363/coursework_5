
def format_vacancies_data(answer_data):
    vacancy_data = {'employers': [],
                    'vacancies': []}
    for data in answer_data:
        vacancy_data['employers'].append({'employer_id': data['items'][0]['employer']['id'],
                                          'employer_name': data['items'][0]['employer']['name'],
                                          'employer_url': data['items'][0]['employer']['alternate_url'],
                                          'vacancy_count': data['found']})
        if not data['items'][0]['salary']:
            data['items'][0]['salary'] = {}
        if not data['items'][0]['snippet']['responsibility']:
            data['items'][0]['snippet']['responsibility'] = data['items'][0]['name']
        vacancy_data['vacancies'].append({'vacancy_id': data['items'][0]['id'],
                                          'employer_id': data['items'][0]['employer']['id'],
                                          'vacancy_title': data['items'][0]['name'],
                                          'description': data['items'][0]['snippet']['responsibility'],
                                          'salary_from': data['items'][0]['salary'].get('from'),
                                          'salary_to': data['items'][0]['salary'].get('to'),
                                          'city': data['items']['area']['name'],
                                          'vacancy_url': data['items'][0]['alternate_url']})
    return vacancy_data
