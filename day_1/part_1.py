from pathlib import Path

from core.helper import read_input_file_to_tuple_of_ints
from core.logger import get_logger
from day_1.day_1_helper import get_sorted_first_and_second_list

logger = get_logger("day_1_part_1")
data = read_input_file_to_tuple_of_ints(f"{Path(__file__).parent}/input.txt")

sorted_first_list, sorted_second_list = get_sorted_first_and_second_list(data)

if len(sorted_first_list) != len(sorted_second_list):
    logger.error("[ERROR]: Lists A and list B are not the same length.")

total = 0

for x in range(len(sorted_first_list)):
    total += abs(sorted_first_list[x] - sorted_second_list[x])

logger.info(f"Total: {total}")
