'Part2: Connecting postgreSQL to Python'
import psycopg2
from config import config
# connection = psycopg2.connect(
#     host="localhost", port="5432", database="master", user="postgres", password="123456")


def connect():
    connection = None
    try:
        params = config()
        print('Connecting to the postgreSQL database ...')
        connection = psycopg2.connect(**params)

        # create a cursor
        crsr = connection.cursor()
        print('PostgreSQL database version: ')
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone()
        print(db_version)
        crsr.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated.')


if __name__ == "__main__":
    connect()
