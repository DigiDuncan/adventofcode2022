from collections import defaultdict
from adventofcode2022.lib.aoc import DayTemplate


class Day(DayTemplate):
    def __init__(self):
        super().__init__(1)
        self.calories = defaultdict(lambda: 0)

        elf = 1
        for line in self.data:
            if line == "":
                elf += 1
            else:
                self.calories[elf] += int(line)

    def part_1(self):
        super().part_1()
        return max(self.calories.values())


    def part_2(self):
        super().part_2()
        return sum(sorted(self.calories.values(), reverse = True)[:3])