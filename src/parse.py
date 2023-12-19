"""This module contains file parsing functions for the trebuchet program.
"""

import logging
import re
from typing import Iterator, List, TextIO, Tuple
from enum import Enum


class Alias(Enum):
    """This enum contains single digit number/word pairs."""

    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9


def parse_file(file: TextIO) -> Iterator[Tuple[str, int]]:
    """Parse the provided file for valid lines.

    Parameters:
        file (TextIO): text file to be parsed.

    Yields:
        A tuple containing the initial string and the integer found
        by concatenating the first and last digit.
    """
    for line in file:
        if line is None:
            yield None

        logging.debug("Parsing %s", line.strip())
        digits = parse_line(line.strip())
        logging.debug("%s parsed from %s", digits, line.strip())

        try:
            result = int(str(digits[0]) + str(digits[-1]))
        except IndexError as e:
            logging.debug("Returning None")
            yield None

        logging.debug("%s returned", result)
        yield (line.strip(), result)


def parse_line(line: str) -> List[int]:
    """Parse the provided string for integers.

    Parameters:
        line (str): the string to parse.

    Returns:
        A list containing all integers found.
    """
    line = "".join(_word_to_digit(list(line)))
    return [int(num) for num in re.findall(r"\d", line)]


def _word_to_digit(line: list) -> list:
    """Convert words in a string to digits.

    Parameters:
        line (list): the string to edit.

    Returns:
        An updated list with the digits replacing
        the numerical words.
    """
    for numbers in Alias:
        has_elem = True
        while has_elem:
            rgx = re.search(str(numbers.name), "".join(line))
            if rgx is not None:
                line.insert(rgx.span()[0] + 1, str(numbers.value))
                logging.debug("Updated String: %s", "".join(line))
            else:
                has_elem = False

    return line
