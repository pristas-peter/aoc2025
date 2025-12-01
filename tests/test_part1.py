from aoc2025.part1 import pt1, pt2

def test_pt1():
    with open('01.test.txt', 'r') as f:
        assert pt1(f.read()) == 3


def test_pt2():
    with open('01.test.txt', 'r') as f:
        assert pt2(f.read()) == 6
