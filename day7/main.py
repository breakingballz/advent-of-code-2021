import statistics
from functools import cache


def process_file(path: str) -> tuple[int, ...]:
    with open(path, "r") as file:
        return tuple(int(val) for val in file.readline().split(","))


@cache
def calc_fuel(num: int) -> int:
    return int(num * (num + 1) / 2)


def run1(positions: tuple[int, ...]) -> int:
    target = round(statistics.median(positions))

    return sum(abs(pos - target) for pos in positions)


def run2(positions: tuple[int, ...]) -> int:
    min_pos = min(pos for pos in positions)
    max_pos = max(pos for pos in positions)

    return min(
        sum(calc_fuel(abs(pos - i)) for pos in positions)
        for i in range(min_pos, max_pos + 1)
    )


def run(path) -> None:
    positions = process_file(path)

    print(f"Result 1: {run1(positions)}")
    print(f"Result 2: {run2(positions)}")



if __name__ == '__main__':
    run("./data.txt")
