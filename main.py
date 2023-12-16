#!/usr/bin/env python3

"""The main module for the trebuchet program.
"""


import click
import logging
from pathlib import Path


@click.command()
@click.version_option("0.1.0", prog_name="trebuchet")
@click.argument(
    "input_file", type=click.Path(exists=True, dir_okay=False, path_type=Path)
)
@click.option(
    "-d", "--debug", is_flag=True, default=False, help="Output debug logs to console"
)
def main(input_file, debug):
    """The main driver for the trebuchet program.

    INPUT_FILE is the file passed in to parse.
    """
    if debug == True:
        logging.basicConfig(level=logging.DEBUG)
    logging.debug(f"{input_file} of type {type(input_file)} accepted")
    return


if __name__ == "__main__":
    main()
