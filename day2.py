from typing import Literal

InputStr = str | Literal["A", "B", "C", "X", "Y", "Z"]
TurnNames = Literal["rock", "paper", "scissors"]
ValidResults = Literal["lose", "draw", "win"]


results: list[ValidResults] = ["lose", "draw", "win"]
turn: list[TurnNames] = ["rock", "paper", "scissors"]


rules: list[list[ValidResults]] = [
    # Rock - Paper - Scissors
    ["draw", "lose", "win"],  # Rock
    ["win", "draw", "lose"],  # Paper
    ["lose", "win", "draw"],  # Scissors
]


def battle(x: InputStr, y: InputStr) -> ValidResults:
    return rules["XYZ".index(x)]["ABC".index(y)]


def calculate_score(move: TurnNames, result: ValidResults) -> int:
    return (turn.index(move) + 1) + (results.index(result) * 3)


def part1(data: list[list[InputStr]]) -> int:
    result = [
        calculate_score(turn["XYZ".index(you)], battle(you, opponent)) for opponent, you in data
    ]
    return sum(result)


def part2(data: list[list[InputStr]]) -> int:
    
    tally = []
    for opp, you in data:
        result = results["XYZ".index(you)]
        your_turn = [item["ABC".index(opp)] for item in rules]
        score = calculate_score(turn[your_turn.index(result)], result)
        tally.append(score)

    return sum(tally)


if __name__ == "__main__":
    with open("inputs/day02_part1.txt") as f:
        data: list[list[InputStr]] = [turn.split(" ") for turn in f.read().splitlines()]

    print(f"{part1(data)=:,}")
    print(f"{part2(data)=:,}")
