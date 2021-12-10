raw = [i.rstrip() for i in open("input.txt", "r").readlines()]


def Part_one(data):
    lowest = []
    file_length = len(data)
    line_length = len(data[0])

    for i in range(file_length):
        line = data[i]

        for j in range(line_length):
            char = int(line[j])

            top = int(data[i - 1][j]) if i != 0 else char
            bottom = int(data[i + 1][j]) if i != file_length - 1 else char

            right = int(line[j + 1]) if j != line_length - 1 else char
            left = int(line[j - 1]) if j != 0 else char

            if char <= left and char <= right and char <= top and char <= bottom and char < 9:
                lowest.append([i, j])

    return lowest


def Follow_point(data, line, pos, basin):
    for y, x in [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]:
        if (line + y, pos + x) not in basin:
            if line + y >= 0 and line + y < len(data):
                if pos + x >= 0 and pos + x < len(data[line]):
                    if data[line + y][pos + x] != '9':
                        basin.add((line + y, pos + x))
                        Follow_point(data, line + y, pos + x, basin)

    return basin


lowest_points = Part_one(raw)
basins = []

for point in lowest_points:
    basin = set()
    basin = Follow_point(raw, point[0], point[1], basin)
    basins.append(len(basin))

*_, third, second, first = sorted(basins)

print(first * second * third)
