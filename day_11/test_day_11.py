from day_11.dumbo_octopus import part_one, part_two

TEST_INPUT = """\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

PART_ONE_TEST_OUTPUT = 1656
PART_TWO_TEST_OUTPUT = 195


def test_part_one():
    assert part_one(TEST_INPUT) == PART_ONE_TEST_OUTPUT


def test_part_two():
    assert part_two(TEST_INPUT) == PART_TWO_TEST_OUTPUT


if __name__ == "__main__":
    test_part_one()
    test_part_two()
