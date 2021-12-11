import re
from pathlib import Path


DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    INITIAL_STATE = f.read()

TEST_INPUT = "3,4,3,1,2"


def perform_day(counters):
    new_counters = []
    for counter in counters:
        if counter == 0:
            new_counters += [6, 8]
        else:
            new_counters.append(counter - 1)

    return new_counters


def part_one(initial_state=INITIAL_STATE, num_days=80):
    counters = [int(n) for n in re.findall("\d+", initial_state)]

    for _ in range(num_days):
        counters = perform_day(counters)

    print(f"There are {len(counters)} lanternfish after {num_days} days")


def part_two(initial_state=INITIAL_STATE, num_days=256):
    part_one(num_days=num_days)


if __name__ == "__main__":
    part_one()
    part_two()
