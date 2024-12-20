from pathlib import Path

from core.helper import read_input_file_to_tuple_of_ints
from core.logger import get_logger
from day_1.day_1_helper import get_first_and_second_list

logger = get_logger("day_2_part_2")
data = read_input_file_to_tuple_of_ints(f"{Path(__file__).parent}/input.txt")

first_list, second_list = get_first_and_second_list(data)

if len(first_list) != len(second_list):
    logger.error("[ERROR]: Lists A and list B are not the same length.")

total = 0

for x in range(len(first_list)):
    number_of_occurrences = len([i for i in second_list if first_list[x] == i])

    if number_of_occurrences != 0:
        logger.info(f"{first_list[x]} occurred {number_of_occurrences} many times")
        total += first_list[x] * number_of_occurrences

logger.info(f"Total: {total}")
