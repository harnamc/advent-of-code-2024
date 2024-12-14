def find_xmas_in_string(xmas_string: str):
    return xmas_string.count("XMAS")


def xmas_string_left_to_right(input: list):
    return sum([find_xmas_in_string(xmas) for xmas in input])


def xmas_string_right_to_left(input: list):
    return sum([find_xmas_in_string(xmas[::-1]) for xmas in input])


def xmas_string_top_to_bottom(input: list):
    return sum(
        [
            find_xmas_in_string(xmas)
            for xmas in ["".join(column) for column in zip(*input)]
        ]
    )


def xmas_string_bottom_to_top(input: list):
    return sum(
        [
            find_xmas_in_string(xmas[::-1])
            for xmas in ["".join(column) for column in zip(*input)]
        ]
    )


def get_diagonal_string_right_to_left(input: list):
    num_rows = len(input)
    max_cols = max(len(row) for row in input)
    diagonals = []

    for diag in range(num_rows + max_cols - 1):
        diagonal = [
            input[row][diag - row]
            for row in range(num_rows)
            if 0 <= diag - row < len(input[row])
        ]
        diagonals.append("".join(diagonal))

    return diagonals


def get_diagonal_string_left_to_right(input: list):
    num_rows = len(input)
    max_cols = max(len(row) for row in input)
    diagonals = []

    for diag in range(-(num_rows - 1), max_cols):
        diagonal = [
            input[row][diag + row]
            for row in range(num_rows)
            if 0 <= diag + row < len(input[row])
        ]
        diagonals.append("".join(diagonal))

    return diagonals
