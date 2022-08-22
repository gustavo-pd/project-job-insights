from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as csv_file:
        readFile = csv.DictReader(csv_file, delimiter=",", quotechar='"')
        return list(readFile)

    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    return []
