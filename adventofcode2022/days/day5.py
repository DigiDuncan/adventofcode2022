from dataclasses import dataclass
import re
import string

from adventofcode2022.lib.aoc import DayTemplate

RE_MOVE = r"move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)"
char = str

@dataclass
class Move:
    x: int
    f: int
    t: int

    def __str__(self) -> str:
        return f"Move: {self.x} from {self.f} to {self.t}"

def visualize_stacks(stacks: list[list[char]]) -> str:
    stack_count = len(stacks)
    max_len = max([len(s) for s in stacks])
    for stack in stacks:
        while len(stack) < max_len:
            stack.insert(0, " ")
    new_lines = []
    for i in range(max_len):
        line = ""
        for j in range(stack_count):
            line += f"{stacks[j][i]} "
        new_lines.append(line)
    return "\n".join(new_lines)

class Day(DayTemplate):
    def __init__(self):
        super().__init__(5)
        SPACING = 4
        self.stacks: list[list[char]] = [[],[],[],[],[],[],[],[],[]]
        self.moves: list[Move] = []
        layout = True
        for line in self.data:
            if line.strip() == "":
                layout = False
                continue
            if layout:
                chunks = [line[i:i+SPACING] for i in range(0, len(line), SPACING)]
                for n, c in enumerate(chunks):
                    try:
                        letter = next(l for l in c if l in string.ascii_uppercase)
                        print(letter, n)
                        self.stacks[n].append(letter)
                    except StopIteration:
                        continue
            else:
                m = re.match(RE_MOVE, line)
                x = int(m.group(1))
                f = int(m.group(2))
                t = int(m.group(3))
                self.moves.append(Move(x, f, t))
        for stack in self.stacks:
            stack.reverse()

    def part_1(self):
        super().part_1()

        print(visualize_stacks(self.stacks))

        for move in self.moves:
            print(move)
            for i in range(move.x):
                try:
                    letter = self.stacks[move.f - 1].pop()
                except IndexError:
                    print(self.stacks)
                    return
                self.stacks[move.t - 1].insert(0, letter)
            print(visualize_stacks(self.stacks))

        s = ""
        for stack in self.stacks:
            s += stack[0]

        return s

    def part_2(self):
        super().part_2()