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

valid_points = set()
intersection_points = set()


def Draw_n_count(adding_points, all_points, saved_intersection):
    intersections = set(all_points.intersection(adding_points))
    saved_intersection = set(saved_intersection.copy().union(intersections))
    all_points = set(all_points.copy().union(adding_points))

    return [all_points, saved_intersection]


for first, second in raw:
    if first[1] == second[1]:
        step = 1 if first[0] < second[0] else -1
        x_list = list(i for i in range(first[0], second[0] + step, step))
        points = set(zip(x_list, [first[1]] * len(x_list)))

        valid_points, intersection_points = Draw_n_count(
            points, valid_points.copy(), intersection_points.copy())

    elif first[0] == second[0]:
        step = 1 if first[1] < second[1] else -1
        y_list = list(i for i in range(first[1], second[1] + step, step))
        points = set(zip([first[0]] * len(y_list), y_list))

        valid_points, intersection_points = Draw_n_count(
            points, valid_points.copy(), intersection_points.copy())

    else:
        step_x = 1 if first[0] < second[0] else -1
        step_y = 1 if first[1] < second[1] else -1
        x_list = list(i for i in range(first[0], second[0] + step_x, step_x))
        y_list = list(i for i in range(first[1], second[1] + step_y, step_y))
        points = set(zip(x_list, y_list))

        valid_points, intersection_points = Draw_n_count(
            points, valid_points.copy(), intersection_points.copy())

print(len(intersection_points))

# End time counter
end_timer = time.perf_counter()
print(end_timer - start_timer)
