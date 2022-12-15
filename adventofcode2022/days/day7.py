from dataclasses import dataclass
from functools import total_ordering
from typing import Union, Callable
import logging

from adventofcode2022.lib.aoc import DayTemplate

logger = logging.getLogger("adventofcode2022")

@dataclass(repr=False)
class File:
    name: str
    size: int

    def __str__(self) -> str:
        return f"{self.name} {self.size}B"

    def __repr__(self) -> str:
        return self.__str__()

    def pstr(self, level = 0) -> str:
        return ("  " * level) + str(self)

@total_ordering
@dataclass(repr=False)
class Directory:
    name: str
    items: list[Union[File, "Directory"]]
    parent: Union["Directory", None] = None

    @property
    def subdirectories(self) -> list["Directory"]:
        return [i for i in self.items if isinstance(i, Directory)]

    @property
    def size(self) -> int:
        return sum(i.size for i in self.items)

    @property
    def path(self) -> str:
        if self.parent is None:
            return "/"
        parent = self.parent
        path = self.parent / self.name
        while parent is not None:
            path = parent.path + path
            parent = parent.parent

    def get(self, name: str) -> Union["Directory", File]:
        return next((i for i in self.items if i.name == name), None)

    def __str__(self) -> str:
        return f"dir {self.name}: {self.size}B"

    def __repr__(self) -> str:
        return self.__str__()

    def pstr(self, level = 0) -> str:
        s = ("  " * level) + "dir " + self.name
        for i in self.items:
            s += "\n" + i.pstr(level + 1)
        return s

    def search(self, criteria: Callable) -> list["Directory"]:
        s = list(filter(criteria, [i for i in self.subdirectories]))
        e = [i.search(criteria) for i in self.subdirectories]
        for l in e:
            s.extend(l)
        return s

    def __lt__(self, other: "Directory"):
        return (self.size, self.name) < (other.size, other.name)

class FileSystem:
    def __init__(self) -> None:
        self.root = Directory("/", [])
        self.current_directory = self.root
        self.max_space = 70000000

    def move_down(self, name: str):
        self.current_directory = self.current_directory.get(name)

    def move_up(self):
        self.current_directory = self.current_directory.parent

    def move_root(self):
        self.current_directory = self.root

    def __str__(self) -> str:
        return str(self.root)

    def __repr__(self) -> str:
        return self.__str__()

    def pstr(self) -> str:
        return self.root.pstr(0)

    def search(self, criteria: callable) -> list[Directory]:
        return self.root.search(criteria)


class Day(DayTemplate):
    def __init__(self):
        super().__init__(7)
        self.filesystem = FileSystem()
        self.parse_tree()

    def parse_tree(self):
        for line in self.data:
            # logger.debug(line)
            if line.startswith("$"):
                line: list[str] = line.split(" ")
                command = line[1]
                if command == "cd":
                    argument = line[2]
                    if argument == "/":
                        self.filesystem.move_root()
                    elif argument == "..":
                        self.filesystem.move_up()
                    else:
                        self.filesystem.move_down(argument)
                elif command == "ls":
                    pass
            else:
                line: list[str] = line.split(" ")
                size = line[0]
                name = line[1]
                if size == "dir":
                    self.filesystem.current_directory.items.append(Directory(name, [], self.filesystem.current_directory))
                else:
                    self.filesystem.current_directory.items.append(File(name, int(size)))

    def part_1(self):
        super().part_1()
        search = self.filesystem.search(lambda x: x.size < 100000)
        print(search)
        return sum(i.size for i in search)

    def part_2(self):
        super().part_2()
        required_free_space = 30000000
        current_free_space = self.filesystem.max_space - self.filesystem.root.size
        to_remove = required_free_space - current_free_space
        search = sorted(self.filesystem.search(lambda x: x.size > to_remove))
        return search[0].size