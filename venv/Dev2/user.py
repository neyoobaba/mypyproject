import psycopg2
from database import connection_pool

class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return "<User {}>".format(self.email)

    def save_to_db(self):
        with connection_pool.getconn() as connection:
            with connection.cursor() as cursor:
                cursor.execute('insert into users (email, first_name, last_name) VALUES (%s, %s, %s)',
                               (self.email, self.first_name, self.last_name))

    # def save_to_db(self):
    #     connection = psycopg2.connect(user='postgres', password='qfalinc5', database='mylearning', hosts='localhost')
    #     with connection.cursor() as cursor:
    #         # Running some code....
    #         cursor.execute('insert into users (email, first_name, last_name) VALUES (%s, %s, %s)', (self.email, self.first_name, self.last_name))
    #     connection.commit()
    #     connection.close()

    @classmethod
    def load_from_db_by_email(cls):
        with connection_pool.getconn as connection:
            with connection.cursor() as cursor:
                cursor.execute('select * from users where email=%s', (email,))
                user_data = cursor.fetchone()
                return cls(email=user_data[1], first_name=user_data[2], last_name=user_data[3], id=user_data[0])
