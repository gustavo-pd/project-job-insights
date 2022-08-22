from src.jobs import read


def get_unique_job_types(path):
    listTypes = set()
    list = read(path)
    for obj in list:
        listTypes.add(obj["job_type"])
    return listTypes


def filter_by_job_type(jobs, job_type):
    list = []
    for obj in jobs:
        if obj["job_type"] == job_type:
            list.append(obj)
    return list


def get_unique_industries(path):
    listIndustries = set()
    list = read(path)
    for obj in list:
        if obj["industry"] != "":
            listIndustries.add(obj["industry"])
    return listIndustries


def filter_by_industry(jobs, industry):
    list = []
    for obj in jobs:
        if obj["industry"] == industry:
            list.append(obj)
    return list


def get_max_salary(path):
    listSalary = []
    list = read(path)
    for obj in list:
        if obj["max_salary"] != "invalid" and \
           obj["max_salary"] != "":
            listSalary.append(int(obj["max_salary"]))
    return max(listSalary)


def get_min_salary(path):
    listSalary = []
    list = read(path)
    for obj in list:
        if obj["min_salary"] != "invalid" and \
           obj["min_salary"] != "":
            listSalary.append(int(obj["min_salary"]))
    return min(listSalary)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
