import time

# Start time counter
start_timer = time.perf_counter()
#

raw = []

with open("input.txt", "r") as input:
    raw_lines = [lines for lines in input.readlines()]
    splited_arrow = list(
        map(lambda x: list((x.rstrip()).split(" -> ")), raw_lines))

    for line in splited_arrow:
        splited_all = []
        splited_comma = list(map(lambda x: x.split(","), line))

        for coors in splited_comma:
            to_int = list(map(int, coors))
            splited_all.append(to_int)

        raw.append(splited_all)


def Find_valid_lines(data):
    same_x = []
    same_y = []
    diagonals = []

    for line in data:
        if line[0][0] == line[1][0]:
            same_x.append(line)
        elif line[0][1] == line[1][1]:
            same_y.append(line)
        else:
            diagonals.append(line)

    return [same_x, same_y, diagonals]


def Update_range(old, new):
    union_set = old.union(new)
    return union_set


def Draw_n_count(key, values, map_dict, saving_dict):
    counter = 0

    if key in map_dict.keys():

        # Testing for intersection
        intersection_set = map_dict[key].intersection(values)

        if len(intersection_set) > 0:
            if key in saving_dict.keys():

                # Check for duplicate
                for i in intersection_set.copy():
                    if i in saving_dict[key]:
                        intersection_set.remove(i)
                    else:
                        saving_dict[key].add(i)
            else:
                saving_dict[key] = intersection_set

            # Update counting points
            for _ in intersection_set:
                counter += 1

        # Update range in dict
        map_dict[key] = Update_range(map_dict[key], values)

    else:
        # Add new key and its set of range
        map_dict[key] = values

    return counter


# Counting same y axis intersections
def Y_intersections(map_dict, saving_dict, y_lines):
    counter = 0

    for first, second in y_lines:
        key = first[1]
        first_value = first[0]
        second_value = second[0]

        step = 1 if first_value < second_value else -1
        values = set(i for i in range(first_value, second_value + step, step))

        counter += Draw_n_count(key, values, map_dict, saving_dict)

    return counter


# Counting x and y intersections
def XY_intersection(map_dict, saving_dict, x_lines):
    counter = 0

    for first, second in x_lines:
        first_key = first[1]
        second_key = second[1]
        value = {first[0]}

        step_key = 1 if first_key < second_key else -1

        for i in range(first_key, second_key + step_key, step_key):
            counter += Draw_n_count(i, value, map_dict, saving_dict)

    return counter


def Diagonals_intersection(map_dict, saving_dict, diag_lines):
    counter = 0

    # Draw diagonals line in a map
    for first, second in diag_lines:
        first_value = first[0]
        first_key = first[1]
        second_value = second[0]
        second_key = second[1]

        step_key = 1 if first_key < second_key else -1
        step_value = 1 if first_value < second_value else -1

        key_list = [
            i for i in range(first_key, second_key + step_key, step_key)
        ]
        value_list = [
            i
            for i in range(first_value, second_value + step_value, step_value)
        ]

        diag_points = list(zip(value_list, key_list))

        for value, key in diag_points:
            counter += Draw_n_count(key, {value}, map_dict, saving_dict)

    return counter


same_x, same_y, diagonals = Find_valid_lines(raw)
counting_dict = dict()
saving_points = dict()
counting_points = 0

counting_points += Y_intersections(counting_dict, saving_points, same_y)
counting_points += XY_intersection(counting_dict, saving_points, same_x)
counting_points += Diagonals_intersection(counting_dict, saving_points,
                                          diagonals)

print(counting_points)

# End time counter
end_timer = time.perf_counter()
print(end_timer - start_timer)
