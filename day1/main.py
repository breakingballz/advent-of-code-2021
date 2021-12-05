NUMS = tuple[int, ...]


def get_numbers(path: str) -> NUMS:
    return tuple(int(val) for val in open(path, "r").readlines())


def run1(nums: NUMS) -> int:
    return sum(
        1 for idx, val in enumerate(nums)
        if len(nums) - idx > 1 and val < nums[idx + 1]
    )


def run2(nums: NUMS) -> int:
    return sum(
        1 for idx, _ in enumerate(nums)
        if len(nums) - idx > 3
        and (
            nums[idx] + nums[idx + 1] + nums[idx + 2]
            < nums[idx + 1] + nums[idx + 2] + nums[idx + 3]
        )
    )


def run(path: str) -> None:
    nums = get_numbers(path)

    print(f"Result 1: {run1(nums)}")
    print(f"Result 2: {run2(nums)}")


if __name__ == "__main__":
    run("./data.txt")
