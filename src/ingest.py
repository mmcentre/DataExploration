import csv
import gzip
import sys
from collections import OrderedDict
from typing import List, Sequence

import psycopg2
import logging

# URL: postgresql+psycopg2://student:secret2@postgres:5432/student
def connect():
    params = {
        "host": "localhost",
        "database": "student",
        "user": "student",
        "password": "secret2"
    }
    return psycopg2.connect(**params)


def import_csv(path: str):
    columns = get_columns(path)
    column_list = ',\n'.join([
        "\t{} {}".format(c, columns[c])
        for c in columns
    ])
    table_ddl = "CREATE TABLE IF NOT EXISTS data_exploration (\n{}\n)"\
        .format(column_list)
    logging.info(table_ddl)

    sql = "COPY data_exploration FROM STDIN WITH " \
          + "(FORMAT CSV, DELIMITER '\t', " \
          + "NULL '(null)', HEADER TRUE, QUOTE '\"')"
    index_ddl = "CREATE INDEX IF NOT EXISTS de_{name}_idx ON data_exploration ({name})"
    with connect() as connection:
        cursor = connection.cursor()
        cursor.execute(table_ddl)
        with gzip.open(path, "rt") as stream:
            next(stream)
            cursor.copy_expert(sql, stream)

        for c in columns:
            if c != 'year' and columns[c] != "VARCHAR":
                continue
            logging.info(index_ddl.format(name=c))
            cursor.execute(index_ddl.format(name=c))



def get_columns(path: str):
    with gzip.open(path, "rt") as stream:
        reader = csv.DictReader(stream, delimiter='\t',
                                quoting = csv.QUOTE_NONE)
        row = next(reader)
        columns = OrderedDict({
            c:
                "VARCHAR" if row[c].startswith('"') else
                "FLOAT" if '.' in row[c] else
                "INT"
            for c in reader.fieldnames
        })
        return columns


def test_connection ():
    with connect() as conn:
        cursor = conn.cursor()

        logging.info('PostgreSQL database version:')
        cursor.execute('SELECT version()')

        db_version = cursor.fetchone()
        logging.info(db_version)

        cursor.close()
    logging.info('Database connection closed.')


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    test_connection()
    cols = get_columns(sys.argv[1])
    print(cols)
    import_csv(sys.argv[1])
