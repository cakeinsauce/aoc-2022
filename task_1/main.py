import utils


def main() -> int:
    lines = utils.get_lines()

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
