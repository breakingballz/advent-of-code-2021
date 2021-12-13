from dataclasses import dataclass
from typing import Optional


@dataclass
class Coord:
    x: int
    y: int


@dataclass
class Point:
    val: int
    coord: Coord
    basin: bool = False
    basin_size: int = 0


MAP = tuple[tuple[Point, ...], ...]


def get_height_map(path: str) -> MAP:
    with open(path, "r") as file:
        return tuple(
            tuple(
                Point(int(val), Coord(x, y))
                for x, val in enumerate(line.replace("\n", ""))
            )
            for y, line in enumerate(file.readlines())
        )


def get_adjacent(point: Point, height_map: MAP) -> tuple[Optional[Point], ...]:
    above, below = point.coord.y - 1, point.coord.y + 1
    left, right = point.coord.x - 1, point.coord.x + 1

    return (
        None if above < 0 else height_map[above][point.coord.x],
        None if below > len(height_map) - 1 else height_map[below][point.coord.x],
        None if left < 0 else height_map[point.coord.y][left],
        None if right > len(height_map[0]) - 1 else height_map[point.coord.y][right],
    )


def get_low_points(height_map: MAP) -> list[Point]:
    points: list[Point] = []

    for row in height_map:
        for point in row:
            above, below, left, right = get_adjacent(point, height_map)

            if (
                (not above or above.val > point.val)
                and (not below or below.val > point.val)
                and (not left or left.val > point.val)
                and (not right or right.val > point.val)
            ):
                points.append(point)

    return points


def run1(height_map: MAP) -> int:
    return sum(point.val + 1 for point in get_low_points(height_map))


def expand(point: Point, height_map: MAP) -> int:
    if point.val == 9 or point.basin:
        return 0

    point.basin = True
    above, below, left, right = get_adjacent(point, height_map)

    return (
        1
        + (expand(above, height_map) if above else 0)
        + (expand(below, height_map) if below else 0)
        + (expand(left, height_map) if left else 0)
        + (expand(right, height_map) if right else 0)
    )


def run2(height_map: MAP) -> int:
    points = get_low_points(height_map)

    for point in points:
        point.basin_size = expand(point, height_map)

    points.sort(key=lambda p: p.basin_size, reverse=True)

    return points[0].basin_size * points[1].basin_size * points[2].basin_size


def run(path: str) -> None:
    height_map = get_height_map(path)

    print(f"Result 1: {run1(height_map)}")
    print(f"Result 2: {run2(height_map)}")


if __name__ == '__main__':
    run("./data.txt")
