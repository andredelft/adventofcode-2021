from pathlib import Path


DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    INPUT_STRING = f.read()


def parse_input(input_string):
    # Parse the input here

    return input_string


def part_one(input_string=INPUT_STRING):
    parsed_input = parse_input(input_string)


def part_two(input_string=INPUT_STRING):
    parsed_input = parse_input(input_string)


if __name__ == "__main__":
    part_one()
    part_two()
