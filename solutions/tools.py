import os


def get_input(filename: str, split_lines=True, cast_to=None):
    with open(os.path.join("..", "input_data", filename), "r") as f:
        data = f.read()

    if split_lines:
        data = data.splitlines()

    if cast_to:
        data = [cast_to(x) for x in data]

    return data
