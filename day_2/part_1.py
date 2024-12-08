from pathlib import Path

from core.helper import read_input_file_to_tuple_of_ints
from core.logger import get_logger
from day_2.day_2_helper import get_level_difference_result

logger = get_logger("day_2_part_1")
current_directory = Path(__file__).parent
reports = read_input_file_to_tuple_of_ints(f"{current_directory}/input.txt")
number_of_safe_reports = 0

for level in reports:
    number_of_safe_reports += all(get_level_difference_result(level))

logger.info(f"Total safe reports: {number_of_safe_reports}")
