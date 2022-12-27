from more_itertools import windowed

with open("inputs/day06_part1.txt") as f:
    data = f.read()


def solution(data: str, n=4) -> int | None:
    for idx, letters in enumerate(windowed(data, n)):
        if len(set(letters)) == n:
            return idx + n
    return None


print(f"Part 1: {solution(data)=:,}")
print(f"Part 2: {solution(data, n=14)=:,}")
