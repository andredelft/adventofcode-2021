from smoke_basin import part_one, part_two

TEST_INPUT = """\
2199943210
3987894921
9856789892
8767896789
9899965678"""

PART_ONE_TEST_OUTPUT = 15
PART_TWO_TEST_OUTPUT = 1134


def test_part_one():
    assert part_one(TEST_INPUT) == PART_ONE_TEST_OUTPUT


def test_part_two():
    assert part_two(TEST_INPUT) == PART_TWO_TEST_OUTPUT


if __name__ == "__main__":
    test_part_one()
    test_part_two()
