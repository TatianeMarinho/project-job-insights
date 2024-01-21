from src.pre_built.counter import count_ocurrences


PATH = "data/jobs.csv"
#   PATHINVALID = "data/jobs_invalid.csv"


def test_counter():
    assert count_ocurrences(PATH, "Python") == 1639
    assert count_ocurrences(PATH, "Java") == 676
#   assert count_ocurrences(PATHINVALID, "Python") == 0
