raw = [i.rstrip() for i in open("./input.txt", "r").readlines()]

instructions = list()
all_points = set()

for i in raw:
    if i != "":
        if i[:4] == "fold":
            instructions.append(i.split(" ")[-1].split("="))
        else:
            all_points.add(tuple(map(int, i.split(","))))


def Fold_the_paper(data, condition_func, new_x, new_y):
    other_side = set(filter(condition_func, data))

    new_all_points = data.difference(other_side)

    for point in other_side:
        new_point = (abs(new_x + point[0]), abs(new_y + point[1]))
        new_all_points.add(new_point)
        data = new_all_points

    return data


def Part_One(data, first_instruction) -> int:
    temp = data.copy()

    direction = first_instruction[0]
    divided_coor = first_instruction[1]
    new_coor = int(divided_coor) * -2

    if direction == "x":
        condition = lambda x: x[0] >= int(divided_coor)
        temp = Fold_the_paper(temp, condition, new_coor, 0)
    else:
        condition = lambda x: x[1] >= int(divided_coor)
        temp = Fold_the_paper(temp, condition, 0, new_coor)

    return len(temp)


def Part_Two(data, instructions):
    temp = data.copy()

    for direction, divided_coor in instructions:
        new_coor = int(divided_coor) * -2

        if direction == "x":
            condition = lambda x: x[0] >= int(divided_coor)
            temp = Fold_the_paper(temp, condition, new_coor, 0)
        else:
            condition = lambda x: x[1] >= int(divided_coor)
            temp = Fold_the_paper(temp, condition, 0, new_coor)

    max_x = 0
    max_y = 0

    for x, y in temp:
        if x > max_x: max_x = x
        if y > max_y: max_y = y

    for i in range(max_y + 1):
        for j in range(max_x + 1):
            if (j, i) in temp:
                print("#", end="")
            else:
                print(" ", end="")

        print()


Part_Two(all_points, instructions)
