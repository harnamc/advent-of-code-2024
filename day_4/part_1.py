from pathlib import Path

from core.helper import read_input_file
from core.logger import get_logger
from day_4.day_4_helper import (
    get_diagonal_string_left_to_right,
    get_diagonal_string_right_to_left,
    xmas_string_bottom_to_top,
    xmas_string_left_to_right,
    xmas_string_right_to_left,
    xmas_string_top_to_bottom,
)

logger = get_logger("day_4_part_1")
input = read_input_file(f"{Path(__file__).parent}/input.txt")
total = 0

# Find XMAS horizontally.
total += xmas_string_left_to_right(input)
total += xmas_string_right_to_left(input)

# Find XMAS vertically.
total += xmas_string_top_to_bottom(input)
total += xmas_string_bottom_to_top(input)

# Find XMAS diagonally.
diagonal_strings_right_to_left = get_diagonal_string_right_to_left(input)
total += xmas_string_left_to_right(diagonal_strings_right_to_left)
total += xmas_string_right_to_left(diagonal_strings_right_to_left)

diagonal_strings_left_to_right = get_diagonal_string_left_to_right(input)
total += xmas_string_left_to_right(diagonal_strings_left_to_right)
total += xmas_string_right_to_left(diagonal_strings_left_to_right)

logger.info(f"Total: {total}")
