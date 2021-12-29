from trick_shot import part_one, part_two

TEST_INPUT = "target area: x=20..30, y=-10..-5"

PART_ONE_TEST_OUTPUT = 45
PART_TWO_TEST_OUTPUT = 112


def test_part_one():
    assert part_one(TEST_INPUT) == PART_ONE_TEST_OUTPUT


def test_part_two():
    assert part_two(TEST_INPUT) == PART_TWO_TEST_OUTPUT


if __name__ == "__main__":
    test_part_one()
    test_part_two()
