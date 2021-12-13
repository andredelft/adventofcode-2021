from pathlib import Path


DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    INPUT = f.read()


def parse_input(input):
    # Parse the input here

    return input


def part_one(input=INPUT):
    parsed_input = parse_input(input)


def part_two(input=INPUT):
    parsed_input = parse_input(input)


if __name__ == "__main__":
    part_one()
    part_two()
