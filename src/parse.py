"""This module contains file parsing functions for the trebuchet program.
"""

from typing import TextIO, Iterator, List, Tuple
import re
import logging


def parse_file(file: TextIO) -> Iterator[Tuple[str, int]]:
    """Parse the provided file for valid lines.

    Parameters:
        file (TextIO): text file to be parsed.

    Yields:
        A tuple containing the initial string and the integer found
        by concatenating the first and last digit.
    """
    for line in file:
        digits = parse_line(line.strip())
        logging.debug("%s parsed from %s", digits, line.strip())

        result = int(str(digits[0]) + str(digits[-1]))

        logging.debug("%s returned", result)
        yield (line.strip(), result)


def parse_line(line: str) -> List[int]:
    """Parse the provided string for integers.

    Parameters:
        line (str): the string to parse.

    Returns:
        A list containing all integers found.
    """
    return [int(num) for num in re.findall(r"\d", line)]
