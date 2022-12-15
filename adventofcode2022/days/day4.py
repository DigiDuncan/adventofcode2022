from adventofcode2022.lib.aoc import DayTemplate

class SectionRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.range = list(range(start, end + 1))

    def is_subset(self, other: "SectionRange"):
        return all([i in self.range for i in other.range])

    def is_overlapping(self, other: "SectionRange"):
        return any([i in self.range for i in other.range])


class Day(DayTemplate):
    def __init__(self):
        super().__init__(4)
        self.pairs: list[tuple[SectionRange]] = []
        for line in self.data:
            l = line.split(",")
            a1, a2 = l[0].split("-")
            b1, b2 = l[1].split("-")
            a = SectionRange(int(a1), int(a2))
            b = SectionRange(int(b1), int(b2))
            self.pairs.append((a, b))

    def part_1(self):
        super().part_1()
        answer = 0
        for p in self.pairs:
            if p[0].is_subset(p[1]) or p[1].is_subset(p[0]):
                answer += 1
        return answer

    def part_2(self):
        super().part_2()
        answer = 0
        for p in self.pairs:
            if p[0].is_overlapping(p[1]) or p[1].is_overlapping(p[0]):
                answer += 1
        return answer