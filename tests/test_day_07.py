from day_07.whale_treachery import part_one, part_two

TEST_INPUT = "16,1,2,0,4,2,7,1,2,14"

PART_ONE_TEST_OUTPUT = 37
PART_TWO_TEST_OUTPUT = 168


def test_part_one():
    assert part_one(TEST_INPUT) == PART_ONE_TEST_OUTPUT


def test_part_two():
    assert part_two(TEST_INPUT) == PART_TWO_TEST_OUTPUT


if __name__ == "__main__":
    test_part_one()
    test_part_two()
