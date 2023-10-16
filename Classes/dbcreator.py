import psycopg2


class DBCreator:
    def __init__(self, set_db_connect, data_for_tables, db_name='headhunter'):
        self.set_db_connect = set_db_connect
        self.data_for_tables = data_for_tables
        self.db_name = db_name

    def create_db(self):
        try:
            conn = psycopg2.connect(dbname='postgres', **self.set_db_connect)
            conn.autocommit = True
            cur = conn.cursor()
            cur.execute(f"DROP DATABASE IF EXISTS {self.db_name}")
            cur.execute(f"CREATE DATABASE {self.db_name}")
            cur.close()
            conn.close()
        except Exception:
            print("Не удалось создать базу данных!")

    def create_tables(self):
        try:
            conn = psycopg2.connect(dbname=self.db_name, **self.set_db_connect)
            with conn.cursor() as cur:
                cur.execute("""
                CREATE TABLE employers (
                employer_id INT PRIMARY KEY,
                employer_name VARCHAR(100) NOT NULL,
                employer_url VARCHAR NOT NULL,
                vacancy_count INT NOT NULL
                )
                """)
            with conn.cursor() as cur:
                cur.execute("""
                CREATE TABLE vacancies (
                vacancy_id INT PRIMARY KEY,
                employer_id INT REFERENCES employers(employer_id),
                vacancy_title TEXT NOT NULL,
                description TEXT NOT NULL,
                salary_from REAL,
                salary_to REAL,
                city VARCHAR(50) NOT NULL,
                vacancy_url TEXT NOT NULL
                )
                """)
            conn.commit()
            conn.close()
        except Exception:
            print("Не удалось создать таблицы!")

    def fill_tables(self):
        try:
            conn = psycopg2.connect(dbname=self.db_name, **self.set_db_connect)
            with conn.cursor() as cur:
                for data in self.data_for_tables['employers']:
                    employer_id = data['employer_id']
                    employer_name = data['employer_name']
                    employer_url = data['employer_url']
                    vacancy_count = data['vacancy_count']
                    cur.executemany("INSERT INTO employers VALUES (%s, %s, %s, %s)",
                                    [(employer_id, employer_name, employer_url, vacancy_count)])
            conn.commit()
            conn.close()
        except Exception:
            print("Ошибка заполнения таблицы employers")

        try:
            conn = psycopg2.connect(dbname=self.db_name, **self.set_db_connect)
            with conn.cursor() as cur:
                for data in self.data_for_tables['vacancies']:
                    vacancy_id = data['vacancy_id']
                    employer_id = data['employer_id']
                    vacancy_title = data['vacancy_title']
                    description = data['description']
                    salary_from = data['salary_from']
                    salary_to = data['salary_to']
                    city = data['city']
                    vacancy_url = data['vacancy_url']
                    cur.executemany("INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                                    [(vacancy_id, employer_id, vacancy_title, description, salary_from, salary_to, city,
                                      vacancy_url)])
            conn.commit()
            conn.close()
        except Exception:
            print("Ошибка заполнения таблицы vacancies")
