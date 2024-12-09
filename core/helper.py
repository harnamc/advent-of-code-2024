def read_input_file_to_tuple_of_ints(file_path):
    with open(file_path, "r") as file:
        return [tuple(map(int, line.split())) for line in file]


def read_input_file(file_path):
    with open(file_path, "r") as file:
        # Need the `line.strip()` to remove the \n that gets added by file.readlines()
        return [line.strip() for line in file.readlines()]
