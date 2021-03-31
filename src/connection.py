import logging

import psycopg2


# URL: postgresql+psycopg2://student:secret2@postgres:5432/student
def connect():
    params = {
        "host": "localhost",
        "database": "student",
        "user": "student",
        "password": "secret2"
    }
    return psycopg2.connect(**params)


def test_connection ():
    with connect() as conn:
        cursor = conn.cursor()

        logging.info('PostgreSQL database version:')
        cursor.execute('SELECT version()')

        db_version = cursor.fetchone()
        logging.info(db_version)

        cursor.close()
    logging.info('Database connection closed.')