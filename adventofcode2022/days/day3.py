from typing import Literal
from adventofcode2022.lib.aoc import DayTemplate

# I decided to take this one in a more object-oriented direction,
# half as a challenge, and half because that's how my brain thinks.

class Rucksack:
    PRIORITY = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, s: str) -> None:
        str_len = len(s) // 2
        self.contents = s
        self.compartment1 = s[0:str_len]
        self.compartment2 = s[str_len:]

    @classmethod
    def get_item_priority(cls, c: str) -> int:
        return cls.PRIORITY.index(c) + 1

    def get_shared_item(self) -> str:
        overlap = set(self.compartment1) & set(self.compartment2)
        return list(overlap)[0]

    def get_shared_item_priority(self) -> int:
        return self.get_item_priority(self.get_shared_item())

    @classmethod
    def get_overlapping_item(cls, rucksacks: list['Rucksack']) -> str:
        contents = [set(r.contents) for r in rucksacks]
        overlap = set.intersection(*contents)
        return list(overlap)[0]

class Day(DayTemplate):
    def __init__(self):
        super().__init__(3)
        self.rucksacks = [Rucksack(line) for line in self.data]

    def part_1(self):
        super().part_1()
        return sum([r.get_shared_item_priority() for r in self.rucksacks])

    def part_2(self):
        super().part_2()
        total = 0
        for i in range(0, len(self.rucksacks), 3):
            rucksacks = self.rucksacks[i:i+3]
            badge = Rucksack.get_overlapping_item(rucksacks)
            badge_priority = Rucksack.get_item_priority(badge)
            total += badge_priority
        return total