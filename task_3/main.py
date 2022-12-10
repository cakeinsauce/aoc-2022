import utils


def item_priority(item: str) -> int:
    if item.islower():
        return ord(item) - 96  # a - z == 1 - 26
    return ord(item) - 38  # A - Z == 27 - 52


def main() -> int:
    priorities_sum = 0
    for items in map(lambda l: l.strip(), utils.get_lines()):
        items_mid = len(items) // 2
        first_comp, second_comp = items[:items_mid], items[items_mid:]
        common_item = list(set(first_comp) & set(second_comp))[0]
        priorities_sum += item_priority(common_item)
    return priorities_sum


if __name__ == "__main__":
    print(main())
