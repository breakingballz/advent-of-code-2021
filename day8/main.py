from collections import Counter

SEQUENCE = tuple[str, ...]
NUMBERS = tuple[str, ...]
DISPLAY = tuple[SEQUENCE, NUMBERS]


def get_displays(path: str) -> list[DISPLAY]:
    result: list[DISPLAY] = []

    with open(path, "r") as file:
        for line in file.readlines():
            sequence, numbers = line.split(" | ")

            result.append((
                tuple(sequence.split(" ")), tuple(numbers.replace("\n", "").split(" "))
            ))

    return result


def run1(displays: list[DISPLAY]) -> int:
    return sum(
        sum(1 for num in numbers if len(num) in (2, 3, 4, 7))
        for _, numbers in displays
    )


def get_decoder(sequence: SEQUENCE) -> dict[str, str]:
    pre_count = {val: key for key, val in Counter("".join(sequence)).items()}
    decoder: dict[str, str] = {"b": pre_count[6], "e": pre_count[4], "f": pre_count[9]}

    values = [*next((val for val in sequence if len(val) == 2))]
    decoder["c"] = next((val for val in values if val not in decoder.values()))
    values = [*next((val for val in sequence if len(val) == 3))]
    decoder["a"] = next((val for val in values if val not in decoder.values()))
    values = [*next((val for val in sequence if len(val) == 4))]
    decoder["d"] = next((val for val in values if val not in decoder.values()))
    values = [*next((val for val in sequence if len(val) == 7))]
    decoder["g"] = next((val for val in values if val not in decoder.values()))

    return {val: key for key, val in decoder.items()}


def decode(numbers: NUMBERS, decoder: dict[str, str]) -> int:
    next_numbers = ["".join([decoder[char] for char in number]) for number in numbers]

    return int(
        "".join(
            [
                {
                    "abcefg": "0",
                    "cf": "1",
                    "acdeg": "2",
                    "acdfg": "3",
                    "bcdf": "4",
                    "abdfg": "5",
                    "abdefg": "6",
                    "acf": "7",
                    "abcdefg": "8",
                    "abcdfg": "9",
                }["".join(sorted(number))]
                for number in next_numbers
            ]
        )
    )


def run2(displays: list[DISPLAY]) -> int:
    return sum(decode(numbers, get_decoder(sequence)) for sequence, numbers in displays)


def run(path: str) -> None:
    displays = get_displays(path)

    print(f"Result 1: {run1(displays)}")
    print(f"Result 2: {run2(displays)}")


if __name__ == "__main__":
    run("./data.txt")
