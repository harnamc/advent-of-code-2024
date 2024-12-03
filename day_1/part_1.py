from pathlib import Path
from core.logger import get_logger


logger = get_logger("day_1")


def read_file(file_path):
    with open(file_path, "r") as file:
        data = [tuple(map(int, line.split())) for line in file]
    return data


current_directory = Path(__file__).parent
data = read_file(f"{current_directory}/input.txt")

sorted_first_list = [x[0] for x in sorted(data, key=lambda x: x[0])]
sorted_second_list = [x[1] for x in sorted(data, key=lambda x: x[1])]

if len(sorted_first_list) != len(sorted_second_list):
    logger.error("[ERROR]: Lists A and list B are not the same length.")

total = 0

for x in range(len(sorted_first_list)):
    total += abs(sorted_first_list[x] - sorted_second_list[x])

logger.info(f"Total: {total}")
