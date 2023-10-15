import os.path
from Classes.dbcreator import DBCreator
from Utils.connection_config import config
from Utils.format_vacancies_data import format_vacancies_data
from Utils.get_vacancies_data import get_vacancies_data, get_emp_data

path_to_connection_config = os.path.join('dbconn.ini')
connect_params = config(filename=path_to_connection_config)

company_ids = [64174, 1740, 4023, 2324020, 328931, 2016792, 4219, 6093, 39305, 1439]
print("Получение данных с сайта hh.ru...")
vacancies_data = get_vacancies_data(company_ids)
emp_data = get_emp_data(company_ids)
vacancies_data_formatted = format_vacancies_data(answer_data_vac=vacancies_data, answer_data_emp=emp_data)
print("Данные получены.")
print("Создание Базы данных и её таблиц...")
db_data = DBCreator(data_for_tables=vacancies_data_formatted, set_db_connect=connect_params)
db_data.create_db()
db_data.create_tables()
db_data.fill_tables()
print("Программа выполнена.")
