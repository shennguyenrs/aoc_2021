raw = [list(map(int, tuple(i.rstrip()))) for i in open("input.txt", "r")]
line_length = len(raw[0])
file_length = len(raw)


def Flashing(pos, line, data, points):
    adjacent_pos = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, 1),
                    (-1, -1), (1, -1)]

    for x, y in adjacent_pos:
        if x + pos >= 0 and y + line >= 0 and x + pos < line_length and y + line < file_length:
            if 0 < data[y + line][x + pos] < 9:
                data[y + line][x + pos] += 1
            elif data[y + line][x + pos] == 9:
                data[y + line][x + pos] = 0
                points.append((x + pos, y + line))
                Flashing(x + pos, y + line, data, points)
            else:
                if (x + pos, y + line) not in points:
                    data[y + line][x + pos] += 1


def Part_one(data):
    counter = 0

    for _ in range(100):
        flashing_points = []
        for line in range(file_length):
            for pos in range(line_length):
                if 0 < data[line][pos] < 9:
                    data[line][pos] += 1
                elif data[line][pos] == 9:
                    data[line][pos] = 0
                    flashing_points.append((pos, line))
                    Flashing(pos, line, data, flashing_points)
                else:
                    if (pos, line) not in flashing_points:
                        data[line][pos] += 1

        counter += len(flashing_points)
        flashing_points.clear()

    return counter


def Part_Two(data):
    step = 0

    while True:
        flashing_points = []

        for line in range(file_length):
            for pos in range(line_length):
                if 0 < data[line][pos] < 9:
                    data[line][pos] += 1
                elif data[line][pos] == 9:
                    data[line][pos] = 0
                    flashing_points.append((pos, line))
                    Flashing(pos, line, data, flashing_points)
                else:
                    if (pos, line) not in flashing_points:
                        data[line][pos] += 1

        if len(flashing_points) == line_length * file_length:
            return step

        step += 1
        flashing_points.clear()


print(Part_Two(raw))
