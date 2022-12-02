def main() -> int:
    with open("input.txt", "r", encoding="ascii") as f_o:
        lines = f_o.readlines()

    most_calories = current_calories = 0
    for line in lines:
        try:
            current_calories += int(line)
        except ValueError:
            most_calories = max(most_calories, current_calories)
            current_calories = 0

    return most_calories


if __name__ == "__main__":
    print(main())
