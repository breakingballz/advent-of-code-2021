from typing import Counter


def get_spawn_timers(path: str) -> tuple[int, ...]:
    with open(path, "r") as file:
        return tuple(
            int(val)
            for val in file.readline().split(",")
        )


def _run(spawn_timers: tuple[int, ...], cycles: int) -> int:
    mapping: dict[int, int] = Counter(spawn_timers)

    for _ in range(0, cycles):
        mapping = {
            val - 1: count
            for val, count in mapping.items()
        }

        if mapping.get(-1) is not None:
            mapping[6] = mapping.get(6, 0) + mapping[-1]
            mapping[8] = mapping[-1]
            del mapping[-1]

    return sum(mapping.values())


def run(path: str) -> None:
    spawn_timers = get_spawn_timers(path)

    print(f"Result 1: {_run(spawn_timers, 80)}")
    print(f"Result 2: {_run(spawn_timers, 256)}")


if __name__ == "__main__":
    run("./data.txt")
