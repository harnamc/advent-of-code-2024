import re
from pathlib import Path

from core.helper import read_input_file
from core.logger import get_logger

logger = get_logger("day_3_part_1")
mul_instruction_regex = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
input = read_input_file(f"{Path(__file__).parent}/input.txt")
input_string = "".join(input)
matches = re.findall(mul_instruction_regex, input_string)
total = sum([int(x) * int(y) for x, y in matches])

logger.info(f"Total: {total}")
