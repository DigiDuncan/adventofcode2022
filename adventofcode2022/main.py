import importlib
import logging
import pkgutil
import re

import digiformatter.logger as digilogger

import adventofcode2022.days as day_modules
from adventofcode2022.lib.aoc import DayTemplate

days: dict[int, DayTemplate] = {}
logger = None

def setup_logging():
    global logger
    logging.basicConfig(level=logging.INFO)
    dfhandler = digilogger.DigiFormatterHandler()
    logger = logging.getLogger("adventofcode2022")
    logger.setLevel(logging.DEBUG)
    logger.handlers = []
    logger.propagate = False
    logger.addHandler(dfhandler)


def load_days():
    # https://stackoverflow.com/a/1708706
    daynames = [name for _, name, _ in pkgutil.walk_packages(day_modules.__path__, prefix = "adventofcode2022.days.")]
    for m in daynames:
        index = re.search(R"day(\d+)", m)
        if index is None:
            continue
        index = int(index.group(1))
        module = importlib.import_module(m)
        days[index] = module.Day()


def main():
    setup_logging()
    load_days()

    i = int(input("Input a day: "))
    if i not in days:
        print("Invalid day.")
    else:
        print(days[i])


if __name__ == "__main__":
    main()