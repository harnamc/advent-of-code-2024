def read_input_file_to_tuple_of_ints(file_path):
    with open(file_path, "r") as file:
        data = [tuple(map(int, line.split())) for line in file]
    return data
