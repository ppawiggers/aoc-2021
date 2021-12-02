from tools import get_input


def clean_input(input_data: str):
    data = get_input(input_data)

    return [(x.split()[0], int(x.split()[1])) for x in data]


def a(input_data: str):
    commands = clean_input(input_data)

    position, depth = 0, 0
    for direction, units in commands:
        if direction == "forward":
            position += units
        elif direction == "up":
            depth -= units
        elif direction == "down":
            depth += units
        else:
            raise Exception("command invalid")

    return position * depth


def b(input_data: str):
    commands = clean_input(input_data)

    position, depth, aim = 0, 0, 0

    for direction, units in commands:
        if direction == "forward":
            position += units
            depth += aim * units
        elif direction == "up":
            aim -= units
        elif direction == "down":
            aim += units
        else:
            raise Exception("command invalid")

    return position * depth


assert a("2a_test.txt") == 150
print(f"a: {a('2a.txt')}")

assert b("2a_test.txt") == 900
print(f"b: {b('2a.txt')}")
