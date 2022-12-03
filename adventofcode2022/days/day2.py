from typing import Literal
from adventofcode2022.lib.aoc import DayTemplate

Move = Literal["R", "P", "S"]
Outcome = Literal["lose", "draw", "win"]

shape_map: dict[str, Move] = {'A': 'R', 'B': 'P', 'C': 'S', 
                              'X': 'R', 'Y': 'P', 'Z': 'S'}

outcome_map: dict[str, Outcome] = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}

score_map: dict[Move | Outcome, int] = {'R': 1, 'P': 2, 'S': 3,
                                        'lose': 0, 'draw': 3, 'win': 6}

def generate_move(enemy: Move, desire: Outcome) -> Move:
    match enemy:
        case "R":
            return {"lose": "S", "draw": "R", "win": "P"}[desire]
        case "P":
            return {"lose": "R", "draw": "P", "win": "S"}[desire]
        case "S":
            return {"lose": "P", "draw": "S", "win": "R"}[desire]

def check_win(enemy: Move, player: Move) -> Outcome:
    check_string = "RPS"
    player_index = check_string.index(player)
    enemy_index = check_string.index(enemy)
    if player_index == enemy_index:
        outcome = "draw"
    elif enemy_index == ((player_index - 1) % 3):
        outcome = "win"
    else: 
        outcome = "lose"
    return outcome

class Day(DayTemplate):
    def __init__(self):
        super().__init__(2)

    def part_1(self):
        super().part_1()
        scores = []
        for line in self.data:
            enemy, player = line.split()
            enemy: Move = shape_map[enemy]
            player: Move = shape_map[player]
            outcome: Outcome = check_win(enemy, player)
            score = score_map[player] + score_map[outcome]
            scores.append(score)
        return sum(scores)

    def part_2(self):
        super().part_2()
        scores = []
        for line in self.data:
            if line == "":
                continue
            enemy, player = line.split()
            enemy: Move = shape_map[enemy]
            outcome: Outcome = outcome_map[player]
            player: Move = generate_move(enemy, outcome)
            score = score_map[player] + score_map[outcome]
            scores.append(score)
        return sum(scores)