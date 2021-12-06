from pathlib import Path

DAY_DIR = Path(__file__).parent

with open(DAY_DIR / "input.txt") as f:
    BINARY_MATRIX = f.read().split("\n")


def bin_to_dec(bin_num: str):
    """Converts a string of 1's and 0's (or truths and falsehoods) to its corresponding decimal number."""

    return sum(2 ** i for (i, n) in enumerate(reversed(list(bin_num))) if int(n))


def part_one(binary_matrix=BINARY_MATRIX):
    column_length = len(binary_matrix)
    row_length = len(binary_matrix[0])

    column_sum = [
        sum(int(binary_matrix[i][j]) for i in range(column_length))
        for j in range(row_length)
    ]

    gamma_rate = bin_to_dec(n > (column_length / 2) for n in column_sum)
    # The gamma and epsilon rate are always each others opposite (bitwise flipped),
    # therefore gamma_rate + epsilon_rate = 111...1 = 2^(colum_length) - 1
    epsilon_rate = (2 ** row_length) - 1 - gamma_rate

    print(gamma_rate * epsilon_rate)


def part_two(binary_matrix=BINARY_MATRIX):
    pass


if __name__ == "__main__":
    part_one()
    part_two()
