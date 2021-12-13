from typing import Iterator


def process_line(line: str) -> tuple[str, int]:
    direction, val = line.split(" ")

    return direction, int(val)


def process_file(path: str) -> Iterator[tuple[str, int]]:
    for line in open(path, "r").readlines():
        yield process_line(line)


def run1(path: str) -> int:
    depth = 0
    horiz = 0

    for direction, val in process_file(path):
        if direction == "forward":
            horiz += val
        elif direction == "down":
            depth += val
        else:
            depth -= val

    return horiz * depth


def run2(path: str) -> int:
    depth = 0
    horiz = 0
    aim = 0

    for direction, val in process_file(path):
        if direction == "forward":
            horiz += val
            depth += aim * val
        elif direction == "down":
            aim += val
        else:
            aim -= val

    return horiz * depth


def run(path: str) -> None:
    print(f"Result 1: {run1(path)}")
    print(f"Result 2: {run2(path)}")


if __name__ == '__main__':
    run("./data.txt")
