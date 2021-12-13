from typing import Callable, Iterator


NUM = tuple[int, ...]
NUMS = tuple[NUM, ...]
COMPARE = Callable[[int], int]


def binary_to_base_10(num: NUM) -> int:
    return int("".join(tuple(str(val) for val in num)), 2)


def get_common(nums: NUMS) -> NUM:
    result = [0 for _ in range(0, len(nums[0]))]

    for item in nums:
        for idx, val in enumerate(item):
            result[idx] += 1 if val else -1

    return tuple(result)


def _get_rating(nums: NUMS, compare_func: COMPARE, idx: int = 0) -> NUMS:
    if not len(nums):
        return tuple()

    if len(nums) == 1:
        return nums

    common = get_common(nums)
    compare = compare_func(common[idx])

    return _get_rating(
        tuple(val for val in nums if val[idx] == compare),
        compare_func,
        idx + 1,
    )


def get_oxygen_rating(nums: NUMS) -> NUMS:
    return _get_rating(nums, lambda d: 0 if d < 0 else 1)


def get_co2_rating(nums: NUMS) -> NUMS:
    return _get_rating(nums, lambda d: 1 if d < 0 else 0)


def process_file(path: str) -> NUMS:
    with open(path, "r") as file:
        return tuple(
            tuple(int(val) for val in line.replace("\n", ""))
            for line in file.readlines()
        )


def run2(nums: NUMS) -> int:
    oxygen_rating = get_oxygen_rating(nums)
    co2_rating = get_co2_rating(nums)

    if not oxygen_rating and co2_rating:
        return 0

    return (
        binary_to_base_10(oxygen_rating[0]) * binary_to_base_10(co2_rating[0])
    )


def run1(nums: NUMS) -> int:
    gamma = tuple(0 if val < 0 else 1 for val in get_common(nums))
    epsilon = tuple(0 if val == 1 else 1 for val in gamma)

    return binary_to_base_10(gamma) * binary_to_base_10(epsilon)


def run(path: str) -> None:
    nums = process_file(path)

    print(f"Result 1: {run1(nums)}")
    print(f"Result 2: {run2(nums)}")


if __name__ == '__main__':
    run("./data.txt")
