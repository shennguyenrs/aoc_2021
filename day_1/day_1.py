raw = []

with open("input.txt", "r") as input:
    raw = [int(line) for line in input.readlines()]


def part_one(data):
    counter = 0

    for i in range(1, len(data)):
        if data[i] > data[i - 1]: counter += 1

    return counter


def part_two(data):
    sum_arr = []

    for i in range(0, len(data) - 2):
        sum_arr.append(data[i] + data[i + 1] + data[i + 2])

    return part_one(sum_arr)


print(part_two(raw))
