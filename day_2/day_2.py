raw = []

with open("input.txt", "r") as input:
    raw = [line for line in input.readlines()]


def part_one(data):
    horizontal = 0
    depth = 0

    for i in data:
        [key, value] = i.split(" ")

        if key == "forward": horizontal += int(value)
        if key == "down": depth += int(value)
        if key == "up": depth -= int(value)

    return horizontal * depth


def part_two(data):
    horizontal = 0
    depth = 0
    aim = 0

    for i in data:
        [key, value] = i.split(" ")

        if key == "forward":
            horizontal += int(value)
            depth += 0 if aim == 0 else aim * int(value)

        if key == "down": aim += int(value)
        if key == "up": aim -= int(value)

    return horizontal * depth


print(part_two(raw))
