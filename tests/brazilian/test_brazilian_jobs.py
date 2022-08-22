from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    jobs = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for obj in jobs:
        assert "title" in obj
        assert "salary" in obj
        assert "type" in obj
