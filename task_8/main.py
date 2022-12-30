import utils


def main() -> int:
    lines = utils.get_lines()
    top_bottom_lines: list[list[int]] = [[] for _ in range(len(lines[0]) - 1)]
    unique_trees: set[tuple[int, int]] = set()

    for y, row in enumerate(lines):
        row_x_heights = tuple(enumerate(map(int, row.strip())))
        max_height_l = max_height_r = -1
        # left to right
        for x, height in row_x_heights:
            top_bottom_lines[x].append(height)
            if height > max_height_l:
                unique_trees.add((x, y))
                max_height_l = height
        # right to left
        # max_height_l contains max tree in a row
        for x, height in reversed(row_x_heights):
            if height > max_height_r:
                unique_trees.add((x, y))
                max_height_r = height
                if max_height_r == max_height_l:
                    break

    for x, column in enumerate(top_bottom_lines):
        column_y_heights = tuple(enumerate(column))
        max_height_t = max_height_b = -1
        # top to bottom
        for y, height in column_y_heights:
            if height > max_height_t:
                unique_trees.add((x, y))
                max_height_t = height
        # bottom to top
        for y, height in reversed(column_y_heights):
            if height > max_height_b:
                unique_trees.add((x, y))
                max_height_b = height
                if max_height_b == max_height_t:
                    break

    return len(unique_trees)


if __name__ == "__main__":
    print(main())
