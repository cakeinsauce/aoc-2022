def get_lines(file_path: str = "input.txt") -> list[str]:
    with open(file_path, "r", encoding="utf-8") as f_o:
        return f_o.readlines()
