from typing import Callable


def process_file(path: str) -> tuple[int, ...]:
    with open(path, "r") as file:
        return tuple(int(val) for val in file.readline().split(","))


def _run(
    positions: tuple[int, ...], fuel_func: Callable[[int], int] = lambda n: n
) -> int:
    min_pos = min(pos for pos in positions)
    max_pos = max(pos for pos in positions)

    return min(
        sum(fuel_func(abs(pos - i)) for pos in positions)
        for i in range(min_pos, max_pos + 1)
    )


def run(path) -> None:
    positions = process_file(path)

    print(f"Result 1: {_run(positions)}")
    print(f"Result 2: {_run(positions, lambda n: int(n * (n + 1) / 2))}")


if __name__ == '__main__':
    run("./data.txt")
