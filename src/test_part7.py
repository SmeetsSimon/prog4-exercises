from .part7 import *


def test_write_numbers_0_100(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "nummers.txt"

    write_numbers(p)

    with open(p, "rt") as f:
        lines = f.readlines()
        assert len(lines) == 100
        expected = [f"{i}\n" for i in range(100)]
        assert lines == expected


def test_write_numbers_and_squares_0_100(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "nummers.txt"

    write_numbers_and_squares(p)

    with open(p, "rt") as f:
        lines = f.readlines()
        assert len(lines) == 100
        expected = [f"{i},{i**2}\n" for i in range(100)]
        assert lines == expected


def test_sum_numbers_from_file_empty(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "nummers.txt"
    with open(p, "wt") as f:
        f.write("")

    result = sum_numbers_from_file(p)

    assert result == 0


def test_sum_numbers_from_file_one(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "nummers.txt"
    with open(p, "wt") as f:
        f.write("42\n")

    result = sum_numbers_from_file(p)

    assert result == 42


def test_sum_numbers_from_file_many_numbers(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "nummers.txt"
    with open(p, "wt") as f:
        f.write("4900\n")
        f.write("90\n")
        f.write("6\n")
        f.write("3\n")
        f.write("1\n")

    result = sum_numbers_from_file(p)

    assert result == 5000


def test_sum_numbers_from_file_empty_lines(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "nummers.txt"
    with open(p, "wt") as f:
        f.write("\n")
        f.write("\n")
        f.write("\n")
        f.write("\n")

    result = sum_numbers_from_file(p)

    assert result == 0


def test_sum_two_columns_of_numbers_from_file_one(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "nummers.txt"
    with open(p, "wt") as f:
        f.write("42,4096\n")

    result = sum_two_columns_of_numbers_from_file(p)

    assert result == (42, 4096)


def test_sum_two_columns_of_numbers_from_file_five(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "nummers.txt"
    with open(p, "wt") as f:
        f.write("4900,10\n")
        f.write("90,5\n")
        f.write("6,9\n")
        f.write("3,1000\n")
        f.write("1,0\n")

    result = sum_two_columns_of_numbers_from_file(p)

    assert result == (5000, 1024)
