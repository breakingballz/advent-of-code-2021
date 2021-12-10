import statistics
import time
from typing import Optional


def process_file(path: str) -> list[str]:
    with open(path, "r") as file:
        return [line.replace("\n", "") for line in file.readlines()]


mapping1 = {")": "(", "]": "[", "}": "{", ">": "<"}
mapping2 = {val: key for key, val in mapping1.items()}
value_mapping1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
value_mapping2 = {")": 1, "]": 2, "}": 3, ">": 4}


def analyze(line: str) -> tuple[str, Optional[int]]:
    sequence: list[str] = []

    for char in line:
        if char in ("(", "[", "{", "<"):
            sequence.append(char)
            continue

        if mapping1[char] == sequence[-1]:
            sequence.pop(-1)
            continue

        if mapping1[char] != sequence[-1]:
            return "CORRUPT", value_mapping1[char]

    return "INCOMPLETE", None


def strip_completed(chars: list[str]) -> list[str]:
    char = chars[0]
    count = 0

    for idx, next_char in enumerate(chars):
        if next_char == char:
            count += 1
            continue

        if next_char == mapping1[char]:
            count -= 1

            if count == 0:
                return chars[idx + 1:]


def get_completion(line: str) -> str:
    if not line:
        return ""

    chars: list[str] = [*line]
    chars.reverse()
    char = chars[0]

    if char in mapping1:
        # Closing char.
        chars = strip_completed(chars)
        chars.reverse()

        return get_completion("".join(chars))

    completion = mapping2[char]

    return completion + get_completion(line + completion)


def run1(lines: list[str]) -> int:
    summ = 0

    for line in lines:
        status, value = analyze(line)

        if status == "CORRUPT" and value:
            summ += value

    return summ


def run2(lines: list[str]) -> int:
    incomplete = [line for line in lines if analyze(line)[0] == "INCOMPLETE"]
    completions = [get_completion(line) for line in incomplete]
    sums: list[int] = []

    for completion in completions:
        summ = 0

        for char in completion:
            summ *= 5
            summ += value_mapping2[char]

        sums.append(summ)

    return statistics.median(sums)


def run(path: str) -> None:
    lines = process_file(path)

    start = time.time()
    print(f"Result 1: {run1(lines)}")
    print("", time.time() - start)
    start = time.time()
    print(f"Result 2: {run2(lines)}")
    print("", time.time() - start)


if __name__ == '__main__':
    run("data.txt")
