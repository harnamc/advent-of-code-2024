ALLOWED_DIFFERENCE = {1, 2, 3}


def get_level_difference_result(level):
    if level[-1] > level[0]:
        return [y - x in ALLOWED_DIFFERENCE for x, y in zip(level, level[1:])]
    else:
        return [x - y in ALLOWED_DIFFERENCE for x, y in zip(level, level[1:])]
