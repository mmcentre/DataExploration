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