def read_file(file_path):
    with open(file_path, "r") as file:
        data = [tuple(map(int, line.split())) for line in file]
    return data


def get_sorted_first_and_second_list(data):
    return [x[0] for x in sorted(data, key=lambda x: x[0])], [
        x[1] for x in sorted(data, key=lambda x: x[1])
    ]


def get_first_and_second_list(data):
    return [x[0] for x in data], [x[1] for x in data]
