# Trebuchet
Python implementation of day 1 of [Advent of Code](https://adventofcode.com/2023/day/1) (2023)

## Requirements
* [Python 3.9+](https://www.python.org/)

## Installation
This project can be installed through `pip install aoc-trebuchet`.

## Running Instructions
This program can be run with the following command: `trebuchet [text file]` in which text file contains
a collection of lines to parse through for integers. The first and last integer found will then be
concatenated. All the final integers from each line will then be added together and the result
written to standard out. 

If this program is run without arguments, the following error message will be outputted: 
`Usage: trebuchet [OPTIONS] INPUT_FILE`

## Sample Execution
When this program is run with `trebuchet resources/example.txt`, the following
output is generated:
`The result is 281`

## Prompt Answer
The answer for part one is **55538**. \
The answer for part two is **54875**.
