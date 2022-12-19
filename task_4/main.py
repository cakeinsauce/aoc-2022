from typing import Tuple

import utils


def is_overlapped(range_1: Tuple[int, int], range_2: Tuple[int, int]) -> bool:
    return (range_1[0] - range_2[0]) * (range_1[1] - range_2[1]) <= 0


def get_range(range_: str) -> Tuple[int, int]:
    return tuple(map(int, range_.split("-")))


def main() -> int:
    overlaps = 0
    for elf_1, elf_2 in map(lambda l: l.strip().split(","), utils.get_lines()):
        if is_overlapped(get_range(elf_1), get_range(elf_2)):
            overlaps += 1
    return overlaps


if __name__ == "__main__":
    print(main())
