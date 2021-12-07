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

    for line in data:
        if line[0][0] == line[1][0]:
            same_x.append(line)
        if line[0][1] == line[1][1]:
            same_y.append(line)

    return [same_x, same_y]


def Update_range(old, new):
    union_set = old.union(new)
    return union_set


def Draw_n_count(key, first, end, data_dict, saving_intersections):
    counter = 0

    if key in data_dict.keys():
        if first < end:
            new_set = set(i for i in range(first, end + 1))
        else:
            new_set = set(i for i in range(end, first + 1))

        # Testing for intersection
        intersection_set = data_dict[key].intersection(new_set)

        if len(intersection_set) > 0:
            if key in saving_intersections.keys():

                # Check for duplicate
                for i in intersection_set.copy():
                    if i in saving_intersections[key]:
                        intersection_set.remove(i)
                    else:
                        saving_intersections[key].add(i)
            else:
                saving_intersections[key] = intersection_set

            # Update counting points
            for _ in range(len(intersection_set)):
                counter += 1

        # Update range in dict
        data_dict[key] = Update_range(data_dict[key], new_set)

    else:
        # Add new key and its set of range
        if first < end:
            data_dict[key] = set(i for i in range(first, end + 1))
        else:
            data_dict[key] = set(i for i in range(end, first + 1))

    return counter


same_x, same_y = Find_valid_lines(raw)
counting_dict = dict()
saving_points = dict()
counting_points = 0

# Counting same y axis intersection
for first, second in same_y:
    key = first[1]
    first_value = first[0]
    second_value = second[0]

    counting_points += Draw_n_count(key, first_value, second_value,
                                    counting_dict, saving_points)

# Counting x and y axis intersection
for first, second in same_x:
    first_key = first[1]
    second_key = second[1]
    value = first[0]

    if first_key < second_key:
        for i in range(first_key, second_key + 1):
            counting_points += Draw_n_count(i, value, value, counting_dict,
                                            saving_points)
    else:
        for i in range(second_key, first_key + 1):
            counting_points += Draw_n_count(i, value, value, counting_dict,
                                            saving_points)

print(counting_points)
