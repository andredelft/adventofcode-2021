from day_06.lanternfish import part_one, part_two

TEST_INPUT = "3,4,3,1,2"

PART_ONE_TEST_OUTPUT = 5934
PART_TWO_TEST_OUTPUT = 26984457539


def test_part_one():
    assert part_one(TEST_INPUT) == PART_ONE_TEST_OUTPUT


def test_part_two():
    assert part_two(TEST_INPUT) == PART_TWO_TEST_OUTPUT
