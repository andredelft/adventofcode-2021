from passage_pathing import part_one, part_two

TEST_INPUT = """\
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

PART_ONE_TEST_OUTPUT = 226
PART_TWO_TEST_OUTPUT = None


def test_part_one():
    assert part_one(TEST_INPUT) == PART_ONE_TEST_OUTPUT


def test_part_two():
    assert part_two(TEST_INPUT) == PART_TWO_TEST_OUTPUT


if __name__ == "__main__":
    test_part_one()
    test_part_two()
