import gzip
import logging

from src.connection import connect
from src.introspection import get_columns


def import_csv(path: str):
    # *******************************************************
    columns = get_columns(path)
    column_list = ',\n'.join([
        "\t{} {}".format(c, columns[c])
        for c in columns
    ])
    table_ddl = "CREATE TABLE IF NOT EXISTS data_exploration (\n{}\n)"\
        .format(column_list)
    logging.info(table_ddl)
    # ********************************************************

    sql = "COPY data_exploration FROM STDIN WITH " \
          + "(FORMAT CSV, DELIMITER '\t', " \
          + "NULL '(null)', HEADER TRUE, QUOTE '\"')"  # QUOTE requires expert mode
    # *********************************************************

    index_ddl = "CREATE INDEX IF NOT EXISTS de_{name}_idx ON data_exploration ({name})"

    with connect() as connection:
        cursor = connection.cursor()
        cursor.execute(table_ddl)
        # *************************

        with gzip.open(path, "rt") as stream:
            next(stream)
            cursor.copy_expert(sql, stream)
        # *************************

        for c in columns:
            if c != 'year' and columns[c] != "VARCHAR":
                continue
            logging.info(index_ddl.format(name=c))
            cursor.execute(index_ddl.format(name=c))