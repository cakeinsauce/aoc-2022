import utils

rock_A = {"X": 3 + 1, "Y": 6 + 2, "Z": 0 + 3}
paper_B = {"X": 0 + 1, "Y": 3 + 2, "Z": 6 + 3}
scissors_C = {"X": 6 + 1, "Y": 0 + 2, "Z": 3 + 3}
outcome_scores = {"A": rock_A, "B": paper_B, "C": scissors_C}


def outcome_score(opponent: str, you: str) -> int:
    return outcome_scores[opponent][you]


def main() -> int:
    rounds = map(lambda l: l.split(), utils.get_lines())
    return sum(map(lambda o_u: outcome_score(o_u[0], o_u[1]), rounds))


if __name__ == "__main__":
    print(main())
