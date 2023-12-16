"""This module contains file parsing functions for the trebuchet program.
"""

from typing import TextIO, Iterator


def parse_file(file: TextIO) -> Iterator[str]:
    """Parse the provided file for valid lines.

    Yields:
        line (str): the next line in the file.
    """
    for line in file:
        yield line.strip()
