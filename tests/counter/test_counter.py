from src.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("tests/mocks/jobs.csv", "Full") == 3
