import importlib.resources as pkg_resources
import logging
import requests
from functools import cache, total_ordering
from typing import Any, Callable

import adventofcode2022.data

logger = logging.getLogger("adventofcode2022")

session = requests.Session()
cookie = pkg_resources.read_text(adventofcode2022.data, "cookie.txt").strip()
requests.utils.add_dict_to_cookiejar(session.cookies, {"session": cookie})


@cache
def get_input_data(day: int) -> list[str]:
    with pkg_resources.path(adventofcode2022.data, f"day{day}.txt") as p:
        if p.exists():
            logger.debug(f"Reading cached data for day {day}.")
            with open(p, "r") as f:
                text = f.read()
        else:
            logger.debug(f"Downloading data for day {day}.")
            url = f"https://adventofcode.com/2022/day/{day}/input"
            text = session.get(url).text
            with pkg_resources.path(adventofcode2022.data, f"day{day}.txt") as p:
                with open(p, "w") as f:
                    f.write(text)
    return [line.strip() for line in text.split("\n")]


@total_ordering
class DayTemplate:
    def __init__(self, day: int, process: Callable[[str], Any] = None):
        """
        Create a new day of the advent calender.
        `day`: an int representing which day this is, for sorting and dynamically grabbing data.
        `process`: a function that can take a string and return any value, since all input data
        is a list of strings and that might not be what we want.
        """
        self.day = day
        self.link = f"https://adventofcode.com/2022/day/{self.day}"
        self._data = get_input_data(self.day)
        self.process = process if process is not None else lambda x: x

    @property
    def data(self) -> list:
        return [self.process(i) for i in self._data]

    def part_1(self) -> Any:
        logger.debug("Calculating part 1...")

    def part_2(self) -> Any:
        logger.debug("Calculating part 2...")

    def __lt__(self, other) -> bool:
        self.day < other.day

    def __eq__(self, other) -> bool:
        self.day == other.day

    def __str__(self) -> str:
        return f"Day {self.day} | {self.part_1()} | {self.part_2()}"