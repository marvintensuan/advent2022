
from typing import Literal, cast

InputStr = str | Literal["A", "B", "C", "X", "Y", "Z" ]
TurnNames = Literal["rock", "paper", "scissors"]
ValidTurns = Literal["win", "lose", "draw"]

mapping: dict[InputStr, TurnNames] = {
    'A': 'rock',
    'X': 'rock',
    'B': 'paper',
    'Y': 'paper',
    'C': 'scissors',
    'Z': 'scissors'
}

scores: dict[ValidTurns, int] = {
    'win' : 6,
    'lose': 0,
    'draw': 3
}

points = {
    'rock'    : 1,
    'paper'   : 2,
    'scissors': 3
}

def battle(x: InputStr, y: InputStr) -> ValidTurns:
    a = mapping[x]
    b = mapping[y]

    if (a == 'scissors') and (b == 'rock'):
        return 'lose'
    if (a == 'rock') and (b == 'scissors'):
        return 'win'
    if a == b:
        return 'draw'
    if points[a] > points[b]:
        return 'win'
    return 'lose'

def calculate_score(move: TurnNames, result: ValidTurns) -> int:
    return points[move] + scores[result]

with open('inputs/day02_part1.txt') as f:
    data: list[list[str]] = [ turn.split(" ") for turn in f.read().splitlines()]
    # data = [
    #     ["A", "Y"],
    #     ["B", "X"]
    # ]

def part1(data: list[list[InputStr]]) -> int:
    result = [
        calculate_score(mapping[you], battle(you, opponent))
        for opponent, you in data
    ]
    return sum(result)

print(f"{part1(data)=:,}")

sample = [[*"AY"],[*"BX"], [*"CZ"]]
