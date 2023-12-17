from pathlib import Path

import pytest

from parse import parse_file, parse_line


@pytest.fixture
def file():
    return Path("./resources/puzzle_input.txt")


class TestParse:
    def test_file_parse(self, file):
        with open(file, "r", encoding="utf-8") as f:
            line = parse_file(f)
            assert next(line) == ("shrzvdcghblt21", 21)
            assert next(line) == ("sixdddkcqjdnzzrgfourxjtwosevenhg9", 99)

    def test_line_parse(self):
        assert parse_line("1abc2") == [1, 2]
        assert parse_line("pqr3stu8vwx") == [3, 8]
        assert parse_line("a1b2c3d4e5f") == [1, 2, 3, 4, 5]
        assert parse_line("treb7uchet") == [7]

        assert parse_line("abc123") == [1, 2, 3]
