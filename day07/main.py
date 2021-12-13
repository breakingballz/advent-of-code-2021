import statistics
import math


def process_file(path: str) -> tuple[int, ...]:
    with open(path, "r") as file:
        return tuple(int(val) for val in file.readline().split(","))


def calc_fuel(num: int) -> int:
    return int(num * (num + 1) / 2)


def run1(positions: tuple[int, ...]) -> int:
    target = round(statistics.median(positions))

    return sum(abs(pos - target) for pos in positions)


def run2(positions: tuple[int, ...]) -> int:
    target = statistics.mean(positions)

    return min(
        sum(calc_fuel(abs(pos - math.floor(target))) for pos in positions),
        sum(calc_fuel(abs(pos - math.ceil(target))) for pos in positions)
    )


def run(path) -> None:
    positions = process_file(path)

    print(f"Result 1: {run1(positions)}")
    print(f"Result 2: {run2(positions)}")


if __name__ == '__main__':
    run("./data.txt")
