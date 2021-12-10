import statistics
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


def strip_completed(line: str) -> str:
    char = line[-1]
    count = 0

    for i in range(len(line) - 1, -1, -1):
        if line[i] == char:
            count += 1
            continue

        if line[i] == mapping1[char]:
            count -= 1

            if count == 0:
                return line[0:i]

    return line


def get_completion(line: str) -> str:
    if not line:
        return ""

    char = line[-1]

    if char in mapping1:
        line = strip_completed(line)

        return get_completion(line)

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

    print(f"Result 1: {run1(lines)}")
    print(f"Result 2: {run2(lines)}")


if __name__ == '__main__':
    run("data.txt")
