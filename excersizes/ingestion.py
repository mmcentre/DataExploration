#  Copyright (c) 2021. Harvard University
#
#  Developed by Michael Bouzinier
#
#  Permission is hereby granted, free of charge, to any person
#  obtaining a copy of this software and associated documentation
#  files (the "Software"), to deal in the Software without restriction,
#  including without limitation the rights to use, copy, modify, merge,
#  publish, distribute, sublicense, and/or sell copies of the Software,
#  and to permit persons to whom the Software is furnished to do
#  so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be
#  included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY
#  OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
#  LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
#  FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
#  NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
#  BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#  WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#  ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import gzip
import logging
import sys

from excersizes.connection import connect
from excersizes.introspection import get_columns


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
            if c not in ['year', 'county_fips'] and columns[c] != "VARCHAR":
                continue
            logging.info(index_ddl.format(name=c))
            cursor.execute(index_ddl.format(name=c))


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    import_csv(sys.argv[1])
