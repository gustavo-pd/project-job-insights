from src.sorting import sort_by

list_jobs = [
    {"min_salary": 2600, "max_salary": 4500, "date_posted": "2020-05-20"},
    {"min_salary": 3300, "max_salary": 8500, "date_posted": "2020-05-05"},
    {"min_salary": 1500, "max_salary": 3000, "date_posted": "2020-05-18"},
]

sorted_min_jobs = [
    {"min_salary": 1500, "max_salary": 3000, "date_posted": "2020-05-18"},
    {"min_salary": 2600, "max_salary": 4500, "date_posted": "2020-05-20"},
    {"min_salary": 3300, "max_salary": 8500, "date_posted": "2020-05-05"},
]

sorted_max_jobs = [
    {"min_salary": 3300, "max_salary": 8500, "date_posted": "2020-05-05"},
    {"min_salary": 2600, "max_salary": 4500, "date_posted": "2020-05-20"},
    {"min_salary": 1500, "max_salary": 3000, "date_posted": "2020-05-18"},
]

list_dates = [
    {"date_posted": "2020-05-18"},
    {"date_posted": "2020-05-05"},
    {"date_posted": "2020-05-02"},
    {"date_posted": "2020-05-20"},
]

list_dates_sorted = [
    {"date_posted": "2020-05-20"},
    {"date_posted": "2020-05-18"},
    {"date_posted": "2020-05-05"},
    {"date_posted": "2020-05-02"},
]


def test_sort_by_criteria():
    sort_by(list_jobs, "min_salary")

    assert list_jobs == sorted_min_jobs
    sort_by(list_jobs, "max_salary")

    assert list_jobs == sorted_max_jobs
    sort_by(list_dates, "date_posted")
    assert list_dates == list_dates_sorted
