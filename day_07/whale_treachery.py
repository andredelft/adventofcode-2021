from pathlib import Path
import re


DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    INPUT = f.read()


def parse_input(input):
    return [int(n) for n in re.findall("\d+", input)]


def part_one(input=INPUT):
    crab_positions = parse_input(input)
    print(crab_positions)


def part_two(input=INPUT):
    parsed_input = parse_input(input)


if __name__ == "__main__":
    part_one()
    part_two()
