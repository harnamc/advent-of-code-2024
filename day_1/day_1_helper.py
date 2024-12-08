def get_sorted_first_and_second_list(data):
    return [x[0] for x in sorted(data, key=lambda x: x[0])], [
        x[1] for x in sorted(data, key=lambda x: x[1])
    ]


def get_first_and_second_list(data):
    return [x[0] for x in data], [x[1] for x in data]
