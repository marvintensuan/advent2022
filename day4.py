PairOfFrozenset = tuple[frozenset, frozenset]


def create_ranges(txt: str) -> tuple[range, range]:
    """Transforms string 'A-B,X-Y' into a 2-tuple of ranges (range(A, B+1), range(X, Y+1))."""
    a, b = txt.split(",")
    lower1, upper1 = [*map(int, a.split("-"))]
    lower2, upper2 = [*map(int, b.split("-"))]
    return (range(lower1, upper1 + 1), range(lower2, upper2 + 1))


def modify_data(data: list[str]) -> list[PairOfFrozenset]:
    """Transforms a list of string 'A-B,X-Y' into a list of type PairOfFrozenSet."""
    as_ranges = [create_ranges(item) for item in data]
    frozendata = [(frozenset(a), frozenset(b)) for (a, b) in as_ranges]
    return frozendata


def fully_contain(first: frozenset, second: frozenset) -> bool:
    """Returns True if all elements of frozenset `first` are in frozenset `second`.
    Otherwise, returns False."""
    drop = first ^ second
    as_set = set(first)
    for item in drop:
        try:
            as_set.remove(item)
        except KeyError:
            return False
    return as_set == second


def overlaps(first: frozenset, second: frozenset) -> bool:
    return len(first & second) > 0


def part1(data: list[PairOfFrozenset]) -> int:
    x = [any([fully_contain(a, b), fully_contain(b, a)]) for a, b in data]
    return sum(x)


def part2(data: list[PairOfFrozenset]) -> int:
    x = [overlaps(a, b) for a, b in data]
    return sum(x)


if __name__ == '__main__':

    with open("inputs/day04_part1.txt") as f:
        data = f.read().splitlines()
        frozendata = modify_data(data)

    print(f"{part1(frozendata)=:,}")
    print(f"{part2(frozendata)=:,}")
