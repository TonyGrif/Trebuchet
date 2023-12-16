import pytest
from pathlib import Path
from parse import parse_file


@pytest.fixture
def file():
    return Path("./resources/puzzle_input.txt")


class TestParse:
    def test_file_parse(self, file):
        with open(file, "r", encoding="utf-8") as f:
            line = parse_file(f)
            assert next(line) == "shrzvdcghblt21"
            assert next(line) == "sixdddkcqjdnzzrgfourxjtwosevenhg9"
