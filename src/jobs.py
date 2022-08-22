from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as csv_file:
        readFile = csv.DictReader(csv_file, delimiter=",", quotechar='"')
        return list(readFile)
