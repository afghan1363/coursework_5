import os.path
from Classes.dbcreator import DBCreator
from Classes.dbmanager import DBManager
from Utils.connection_config import config
from Utils.format_vacancies_data import format_vacancies_data
from Utils.get_vacancies_data import get_vacancies_data, get_emp_data


def query_create_db():
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


def user_interface():
    flag = 5
    while flag == 5:
        choice = input("""1 - Создать базу данных и заполнить таблицы        
2 - Получить данные из базы данных
0 - Выход
""")
        if choice == "0":
            flag = 0
            break
        elif choice == "1":
            query_create_db()
        elif choice == "2":
            flag = 6
    while flag == 6:
        path_to_connection_config = os.path.join('dbconn.ini')
        connect_params = config(filename=path_to_connection_config)
        answer = input("""Выбери номер запроса:
1 - Получить список всех компаний и количество вакансий у каждой компании.
2 - Получить список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
3 - Получить среднюю зарплату по вакансиям.
4 - Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям.
5 - Получить список всех вакансий, в названии которых содержатся переданные в метод слова.
0 - Выход
10 - Обновить Базу данных
""")
        db_manager = DBManager(set_db_connect=connect_params)
        if answer == "1":
            db_manager.get_companies_and_vacancies_count()
        elif answer == "2":
            db_manager.get_all_vacancies()
        elif answer == "3":
            db_manager.get_avg_salary()
        elif answer == "4":
            db_manager.get_vacancies_with_higher_salary()
        elif answer == "5":
            key = input("Введите слово для поиска: ")
            db_manager.get_vacancies_with_keyword(keyword=key)
        elif answer == "0":
            break
        else:

            user_interface()
