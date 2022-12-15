from adventofcode2022.lib.aoc import DayTemplate

def are_chars_unique(s: str) -> bool:
    return len(list(set(s))) == len(s)

def view_window(s: str, l: int, i: int) -> str:
    return s[i:i+l] if len(s) > i+l else s[i:]


class Day(DayTemplate):
    def __init__(self):
        super().__init__(6)
        self.stream: str = self.data[0]
        self.HEADER_LENGTH = 4
        self.MESSAGE_LENGTH = 14

    def part_1(self):
        super().part_1()
        for i in range(len(self.stream)):
            window = view_window(self.stream, self.HEADER_LENGTH, i)
            if are_chars_unique(window):
                return i + self.HEADER_LENGTH


    def part_2(self):
        super().part_2()
        for i in range(len(self.stream)):
            window = view_window(self.stream, self.MESSAGE_LENGTH, i)
            if are_chars_unique(window):
                return i + self.MESSAGE_LENGTH