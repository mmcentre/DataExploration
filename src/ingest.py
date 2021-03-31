import sys

import logging

from src.connection import test_connection
from src.introspection import get_columns
from src.loading import import_csv

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    test_connection()
    cols = get_columns(sys.argv[1])
    print(cols)
    import_csv(sys.argv[1])
