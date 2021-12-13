GRID = tuple[list[int], ...]
COORD = tuple[int, int]


def process_file(path: str) -> GRID:
    with open(path, "r") as file:
        return tuple(
            [int(val) for val in line.replace("\n", "")]
            for line in file.readlines()
        )


def get_adjacent_coords(coord: COORD, max_x: int, max_y: int) -> list[COORD]:
    x, y = coord
    next_coords: list[COORD] = []

    for next_y in range(-1, 2):
        for next_x in range(-1, 2):
            final_y = y + next_y
            final_x = x + next_x

            if (
                -1 < final_y < max_y
                and -1 < final_x < max_x
                and (final_x, final_y) != coord
            ):
                next_coords.append((final_x, final_y))

    return next_coords


def get_flashes(grid: GRID) -> int:
    flashes = 0

    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col >= 10:
                flashes += 1
                grid[y][x] = 0
                adjacent = get_adjacent_coords((x, y), len(grid[0]), len(grid))

                for next_x, next_y in adjacent:
                    if grid[next_y][next_x] == 0:
                        continue

                    grid[next_y][next_x] += 1

    if not flashes:
        return 0

    return flashes + get_flashes(grid)


def step_grid(grid: GRID) -> int:
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            grid[y][x] += 1

    return get_flashes(grid)


def run1(path: str) -> int:
    grid = process_file(path)
    
    return sum(step_grid(grid) for _ in range(0, 100))


def run2(path: str) -> int:
    grid = process_file(path)
    step = 0

    while sum(sum(col for col in row)for row in grid) > 0:
        step_grid(grid)
        step += 1

    return step


def run(path: str) -> None:
    print(f"Result 1: {run1(path)}")
    print(f"Result 2: {run2(path)}")


if __name__ == '__main__':
    run("./data.txt")
