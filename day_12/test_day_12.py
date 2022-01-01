from passage_pathing import part_one, part_two

TEST_INPUT = """\
start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

PART_ONE_TEST_OUTPUT = 10
PART_TWO_TEST_OUTPUT = 36


def test_part_one():
    assert part_one(TEST_INPUT) == PART_ONE_TEST_OUTPUT


def test_part_two():
    assert part_two(TEST_INPUT) == PART_TWO_TEST_OUTPUT


if __name__ == "__main__":
    # test_part_one()
    test_part_two()
