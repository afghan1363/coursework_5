import psycopg2


class DBManager:

    def __init__(self, set_db_connect, db_name='headhunter'):
        self.set_db_connect = set_db_connect
        self.db_name = db_name
        self.conn = psycopg2.connect(dbname=self.db_name, **self.set_db_connect)
        self.cursor = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество
        вакансий у каждой компании."""
        self.cursor.execute("""SELECT employer_name, vacancy_count FROM employers;""")
        answer = self.cursor.fetchall()
        for data in answer:
            print(f"Компания: {data[0]};  Количество вакансий: {data[1]}")

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию."""
        self.cursor.execute("""SELECT employers.employer_name, vacancy_title, salary_from, salary_to, vacancy_url
        FROM vacancies
        RIGHT JOIN employers
        USING(employer_id);""")
        answer = self.cursor.fetchall()
        for data in answer:
            salary_from = data[2]
            salary_to = data[3]
            if not data[2]:
                salary_from = 'Не указано'
            if not data[3]:
                salary_to = 'Не указано'
            print(f"Компания: {data[0]}; Вакансия: {data[1]}; Зарплата от - до: {salary_from} - {salary_to};\
             Ссылка: {data[4]}")

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям."""
        self.cursor.execute("""SELECT AVG((salary_from + salary_to) / 2)
        FROM vacancies;""")
        answer = self.cursor.fetchall()[0][0]
        print(f"Средняя зарплата по вакансиям: {answer}")

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата
        выше средней по всем вакансиям."""
        self.cursor.execute("""SELECT vacancy_title, description, vacancy_url
        FROM vacancies
        WHERE salary_from > (SELECT AVG((salary_from+salary_to) / 2) FROM vacancies)
        ORDER BY salary_from DESC;""")
        answer = self.cursor.fetchall()
        for data in answer:
            print(f"Вакансия: {data[0]};\nОписание: {data[1]};\nСсылка: {data[2]}\n")

    def get_vacancies_with_keyword(self, keyword):
        """Получает список всех вакансий, в названии которых содержатся переданные
        в метод слова"""
        self.cursor.execute(f"""SELECT vacancy_title, description, vacancy_url
        FROM vacancies
        WHERE vacancy_title ILIKE '%{keyword}%'
        OR description ILIKE '%{keyword}%';""")
        answer = [print(data) for data in self.cursor.fetchall()]
        return answer
