import re

COORD = tuple[int, int]
PAIR = tuple[COORD, COORD]


def process_line(line: str) -> PAIR:
    match = re.match(r"^(\d+),(\d+) -> (\d+),(\d+)$", line)

    if not match:
        raise ValueError("Invalid data")

    return (
        (int(match.group(1)), int(match.group(2))),
        (int(match.group(3)), int(match.group(4))),
    )


def process_file(path: str):
    with open(path, "r") as f:
        return [process_line(line) for line in f.readlines()]


def get_straight_path(pair: PAIR) -> list[COORD]:
    coord1, coord2 = pair
    result: list[COORD] = []
    min_y = min(coord1[1], coord2[1])
    min_x = min(coord1[0], coord2[0])

    for y in range(0, abs(coord1[1] - coord2[1]) + 1):
        for x in range(0, abs(coord1[0] - coord2[0]) + 1):
            result.append((x + min_x, y + min_y))

    return result


def get_diagonal_path(pair: PAIR) -> list[COORD]:
    coord1, coord2 = pair
    x_incr = 1 if coord1[0] < coord2[0] else -1
    y_incr = 1 if coord1[1] < coord2[1] else -1

    return [
        (coord1[0] + i * x_incr, coord1[1] + i * y_incr)
        for i in range(0, abs(coord1[0] - coord2[0]) + 1)
    ]


def get_path(pair: PAIR) -> list[COORD]:
    if pair[0][0] == pair[1][0] or pair[0][1] == pair[1][1]:
        return get_straight_path(pair)

    return get_diagonal_path(pair)


def _run(coord_pairs: list[PAIR]) -> int:
    result: dict[COORD, int] = {}

    for pair in coord_pairs:
        for coord in get_path(pair):
            result[coord] = result.get(coord, 0) + 1

    return len(tuple(val for val in result.values() if val > 1))


def run(path: str) -> None:
    coord_pairs2 = process_file(path)
    coord_pairs = [
        pair for pair in coord_pairs2
        if pair[0][0] == pair[1][0] or pair[0][1] == pair[1][1]
    ]

    print(f"Result 1: {_run(coord_pairs)}")
    print(f"Result 2: {_run(coord_pairs2)}")


if __name__ == '__main__':
    run("./data.txt")
