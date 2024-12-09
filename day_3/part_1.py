import re

from core.logger import get_logger
from day_3.input import mul_instructions

logger = get_logger("day_3_part_1")
mul_instruction_regex = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
matches = re.findall(mul_instruction_regex, mul_instructions)
total = sum([int(x) * int(y) for x, y in matches])

logger.info(f"Total: {total}")
