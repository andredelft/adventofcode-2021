from pathlib import Path
import re

DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    LINES = f.read()

TEST_INPUT = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def parse_input(lines=LINES):
    coordinates = []

    for line in lines.split("\n"):
        x1, y1, x2, y2 = [int(n) for n in re.findall(r"\d+", line)]
        coordinates.append([(x1, y1), (x2, y2)])

    return coordinates


def part_one(lines=LINES):
    coordinates = parse_input(lines)

    x_max = 0
    y_max = 0

    for ((x1, y1), (x2, y2)) in coordinates:
        x = max(x1, x2)
        y = max(y1, y2)

        if x > x_max:
            x_max = x
        if y > y_max:
            y_max = y

    print(f"Field dimensions: {x_max} x {y_max}")

    field = [[0 for _ in range(x_max + 1)] for _ in range(y_max + 1)]

    for ((x1, y1), (x2, y2)) in coordinates:
        if x1 == x2:
            y_from = min(y1, y2)
            y_to = max(y1, y2)
            for y in range(y_from, y_to + 1):
                field[x1][y] += 1
        elif y1 == y2:
            x_from = min(x1, x2)
            x_to = max(x1, x2)
            for x in range(x_from, x_to + 1):
                field[x][y1] += 1

    # print("\n".join(" ".join(f"{n: >2}" for n in row) for row in field))

    num_crossroads = 0

    for x in range(x_max + 1):
        for y in range(y_max + 1):
            if field[x][y] >= 2:
                num_crossroads += 1

    print(f"{num_crossroads} number of crossroads found")


def part_two(lines=LINES):
    coordinates = parse_input(lines)

    x_max = 0
    y_max = 0

    for ((x1, y1), (x2, y2)) in coordinates:
        x = max(x1, x2)
        y = max(y1, y2)

        if x > x_max:
            x_max = x
        if y > y_max:
            y_max = y

    print(f"Field dimensions: {x_max} x {y_max}")

    field = [[0 for _ in range(x_max + 1)] for _ in range(y_max + 1)]

    for ((x1, y1), (x2, y2)) in coordinates:
        if x1 == x2:
            y_from = min(y1, y2)
            y_to = max(y1, y2)
            for y in range(y_from, y_to + 1):
                field[x1][y] += 1
        elif y1 == y2:
            x_from = min(x1, x2)
            x_to = max(x1, x2)
            for x in range(x_from, x_to + 1):
                field[x][y1] += 1
        else:
            pass  # TODO: Handle diagonals!

    # print("\n".join(" ".join(f"{n: >2}" for n in row) for row in field))

    num_crossroads = 0

    for x in range(x_max + 1):
        for y in range(y_max + 1):
            if field[x][y] >= 2:
                num_crossroads += 1

    print(f"{num_crossroads} number of crossroads found")


if __name__ == "__main__":
    part_one()
