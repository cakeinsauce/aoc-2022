import utils


def main() -> str:
    lines = utils.get_lines()
    stack_lines = lines[:8]
    move_lines = lines[10:]
    sorted_stacks = [[] for _ in range(9)]  # len = 9
    for stack_line in map(lambda l: l.rstrip("\n"), stack_lines[::-1]):
        skipped_spaces = 0
        stack_i = 0
        for char in stack_line:  # type: str
            if char.isalpha():
                sorted_stacks[stack_i].append(char)
                stack_i += 1
                skipped_spaces = 0
            elif char.isspace():
                skipped_spaces += 1
            if skipped_spaces == 4:
                stack_i += 1
                skipped_spaces = 0

    for move in move_lines:
        n_box, stack_i_from, stack_i_to = map(int, move.split(" ")[1::2])
        crane = sorted_stacks[stack_i_from - 1][-n_box:][::-1]
        sorted_stacks[stack_i_from - 1] = sorted_stacks[stack_i_from - 1][:-n_box]
        sorted_stacks[stack_i_to - 1].extend(crane)

    return "".join(b[-1] if b else " " for b in sorted_stacks)


if __name__ == "__main__":
    print(main())
