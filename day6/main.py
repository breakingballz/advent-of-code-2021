class Lanternfish:
    spawn_timer: int
    children: list["Lanternfish"]
    first_cycle: bool

    def __init__(self, spawn_timer: int = 8) -> None:
        self.spawn_timer = spawn_timer
        self.children = []
        self.first_cycle = spawn_timer == 8

    def tick(self) -> None:
        self.spawn_timer -= 1
        self.spawn_timer = 6 if self.spawn_timer == -1 else self.spawn_timer

        if self.spawn_timer == 0:
            self.first_cycle = False

        if self.first_cycle:
            return

        for child in self.children:
            child.tick()

        if self.spawn_timer == 6:
            self.children.append(Lanternfish())

    def __repr__(self) -> str:
        return (
            f"Lanternfish(spawn_timer={self.spawn_timer}, "
            f"first_cycle={self.first_cycle} children={self.children})"
        )

    @property
    def descendants(self) -> int:
        return (
            len(self.children)
            + sum(child.descendants for child in self.children)
        )


def get_spawn_timers(path: str) -> tuple[int, ...]:
    with open(path, "r") as file:
        return tuple(
            int(val)
            for val in file.readline().split(",")
        )


def _run(spawn_timers: tuple[int, ...], cycles: int) -> int:
    lanternfish = [Lanternfish(spawn_timer) for spawn_timer in spawn_timers]

    for _ in range(0, cycles):
        for fish in lanternfish:
            fish.tick()

    return (
        len(lanternfish)
        + sum(fish.descendants for fish in lanternfish)
    )


def run1(spawn_timers: tuple[int, ...]) -> int:
    lanternfish = [Lanternfish(spawn_timer) for spawn_timer in spawn_timers]

    for _ in range(0, 80):
        for fish in lanternfish:
            fish.tick()

    return (
        len(lanternfish)
        + sum(fish.descendants for fish in lanternfish)
    )


def run(path: str) -> None:
    spawn_timers = get_spawn_timers(path)

    print(f"Result 1: {_run(spawn_timers, 80)}")
    print(f"Result 2: {_run(spawn_timers, 256)}")


if __name__ == "__main__":
    run("./data.txt")
