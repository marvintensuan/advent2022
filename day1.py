
NestedListOfInt = list[list[int]]

with open('inputs/day01_part1.txt') as f:
    data: NestedListOfInt = [ [*(map(int, el.splitlines()))] for el in f.read().split('\n\n')]

def part1(data: NestedListOfInt) -> int:
    r = [sum(el) for el in data]
    return max(r)

def part2(data: NestedListOfInt) -> int:
    r = sorted([sum(el) for el in data], reverse=True)
    return sum(r[:3])

print(f"{part1(data)=:,}")
print(f"{part2(data)=:,}")
