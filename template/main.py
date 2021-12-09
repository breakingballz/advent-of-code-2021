def process_file(path: str) -> list[str]:
    with open(path, "r") as file:
        return [line.replace("\n", "") for line in file.readlines()]


def run1(lines: list[str]) -> int:
    pass  # TODO: Impl.


def run2(lines: list[str]) -> int:
    pass  # TODO: Impl.


def run(path: str) -> None:
    lines = process_file(path)

    print(f"Result 1: {run1(lines)}")
    print(f"Result 2: {run2(lines)}")


if __name__ == '__main__':
    run("data.txt")
