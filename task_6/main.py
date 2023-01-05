import utils


def main() -> int:
    signal_seq = utils.get_lines()[0].strip()
    for i in range(len(signal_seq)):
        four_chars = signal_seq[i:i + 4]
        if len(set(four_chars)) == 4:
            return i + 4


if __name__ == "__main__":
    print(main())
