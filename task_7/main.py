from collections import defaultdict

import utils


def main() -> int:
    commands = map(lambda l: l.strip(), utils.get_lines())
    directories: dict[str, int] = defaultdict(int)
    current_path: list[str] = []
    for prefix, args in map(lambda c: c.split(" ", 1), commands):
        if prefix == "$":
            if not args.startswith("cd"):
                continue
            path_to = args.split(" ")[1]
            if path_to == "/":
                continue
            if path_to == "..":
                current_path.pop()
            else:
                current_path.append(path_to)
        else:
            try:
                file_size = int(prefix)
            except ValueError:
                continue

            file_dir = ""
            for dir_ in current_path:
                file_dir += f"/{dir_}"
                directories[file_dir] += file_size
    return sum(size for size in directories.values() if size <= 100_000)


if __name__ == "__main__":
    print(main())
