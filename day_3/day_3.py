raw = []

with open("input.txt", "r") as input:
    raw = [line for line in input.readlines()]


def contrary_binary(binary):
    result = ""
    for i in range(0, len(binary)):
        result += "1" if binary[i] == "0" else "0"

    return result


def part_one(data):
    length = len(data)
    row_length = len(data[0]) - 1  # To remove the \n of the string
    sum_row = [0] * row_length
    gamma = ""

    for line in data:
        for i in range(0, row_length):
            sum_row[i] += int(line[i])

    for i in range(0, row_length):
        remain = length - sum_row[i]

        gamma += "0" if remain > sum_row[i] else "1"

    epsilon = contrary_binary(gamma)

    return int(gamma, 2) * int(epsilon, 2)


def part_two(data, index, length, row_length, rating):
    sum_row = 0

    if index == row_length:
        return data
    else:
        for line in data:
            sum_row += int(line[index])

        remain = length - sum_row

        if rating == "o2":
            temp = filter(
                lambda x: x[index] == ("1"
                                       if sum_row >= remain else "0"), data)
        else:
            temp = filter(
                lambda x: x[index] == ("0"
                                       if remain <= sum_row else "1"), data)

        data = list(temp)
        new_length = len(data)

        if new_length == 1:
            return data
        else:
            index += 1
            return part_two(data, index, new_length, row_length, rating)


row_length = len(raw[0]) - 1
oxy_rating_binary = part_two(raw, 0, len(raw), row_length, "o2")[0][:-1]
co2_rating_binary = part_two(raw, 0, len(raw), row_length, "co2")[0][:-1]

print(int(oxy_rating_binary, 2) * int(co2_rating_binary, 2))
