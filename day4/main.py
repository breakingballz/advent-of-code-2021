from typing import Optional


NUMS = list[int]
BOARD = list[list[Optional[int]]]
BOARDS = list[BOARD]


def process_file(path: str) -> tuple[NUMS, BOARDS]:
    with open(path, "r") as f:
        lines = f.readlines()

        boards: list[BOARD] = []

        for i in range(2, len(lines), 6):
            board: BOARD = []

            for j in range(0, 5):
                board.append([
                    int(val) for val
                    in lines[i + j].replace("\n", "").split(" ")
                    if val
                ])

            boards.append(board)

    return [int(val) for val in lines[0].split(",")], boards


def process_board(board: BOARD, num: int) -> None:
    for row in board:
        for idx, col in enumerate(row):
            if col == num:
                row[idx] = None


def get_empty_board() -> BOARD:
    board: BOARD = []

    for i in range(0, 5):
        board.append([None for _ in range(0, 5)])

    return board


def check_sequence(row: list[Optional[int]]) -> bool:
    return not len([val for val in row if val is not None])


def winning_board(board: BOARD) -> bool:
    for row in board:
        if check_sequence(row):
            return True

    inverse: BOARD = get_empty_board()

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            inverse[j][i] = col

    for row in inverse:
        if check_sequence(row):
            return True

    return False


def get_winner(boards: BOARDS, num: int) -> Optional[BOARD]:
    for board in boards:
        process_board(board, num)

        if winning_board(board):
            return board

    return None


def get_winners(boards: BOARDS, num: int) -> list[BOARD]:
    winning_boards: list[BOARD] = []

    for board in boards:
        process_board(board, num)

        if winning_board(board):
            winning_boards.append(board)

    return winning_boards


def run1(path: str) -> int:
    nums, boards = process_file(path)

    for num in nums:
        winner = get_winner(boards, num)

        if winner:
            amount = sum(
                sum(val for val in row if val is not None)
                for row in winner
            )

            return amount * num

    raise ValueError("No winners")


def run2(path: str) -> int:
    nums, boards = process_file(path)
    candidates: list[BOARD] = []
    candidate_num = 0

    for num in nums:
        winners = get_winners(boards, num)

        if winners:
            candidates = winners
            candidate_num = num

            for idx, board in enumerate(boards):
                if board in winners:
                    del boards[idx]

    if not candidates:
        raise ValueError("No winners")

    return sum(
        sum(val for val in row if val is not None)
        for row in candidates[0]
    ) * candidate_num


def run(path: str) -> None:
    print(f"{run1(path)}")
    print(f"{run2(path)}")


if __name__ == '__main__':
    run("./data.txt")
