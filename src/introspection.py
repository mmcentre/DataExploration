import csv
import gzip
from collections import OrderedDict


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