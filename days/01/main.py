import re
from functools import reduce

def part1(left, right):
    return sum(abs(r - l) for r, l in zip(left, right))

def part2(left, right):
    occurrences = reduce(lambda acc, v: acc | { v: acc.get(v, 0) + 1 }, right, {})
    return sum([occurrences.get(l, 0) * l for l in left])

def part2_slow(left, right):
    return sum([right.count(l) * l for l in left])

def main():
    # Transform input
    file = open('input/day1.txt', 'r')
    lines = [re.split(r'\s+', line.strip()) for line in file.readlines()]
    lines = [(int(l), int(r)) for l, r in lines]
    left, right = map(sorted, zip(*lines))

    # Part 1
    result1 = part1(left, right)
    print('result1', result1)
    assert result1 == 1603498

    # Part 2
    result2 = part2(left, right)
    print('result2', result2)
    assert result2 == 25574739

if __name__ == "__main__":
    print('day 01')
    main()