from tools import get_input


def clean_input(input_data: str):
    return get_input(input_data, cast_to=int)


def a(input_data: str):
    data = clean_input(input_data)

    return sum([data[i] > data[i - 1] for i in range(1, len(data))])


def b(input_data: str):
    data = clean_input(input_data)

    def window(d, i):
        return d[i] + d[i - 1] + d[i - 2]

    return sum([window(data, i) > window(data, i - 1) for i in range(3, len(data))])


assert a("1a_test.txt") == 7
print(f"a: {a('1a.txt')}")

assert b("1a_test.txt") == 5
print(f"b: {b('1a.txt')}")
