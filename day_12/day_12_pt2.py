raw = [i.rstrip().split("-") for i in open("./input.txt", "r")]


def Add_edge(map_dict, key, value):
    if key not in map_dict.keys():
        map_dict[key] = [value]
    else:
        map_dict[key].append(value)


def Find_paths(map_dict,
               current_pos,
               path=[],
               visted=dict(),
               allow_visting_this_cave=True):
    path = path + [current_pos]

    if current_pos == "end":
        return [path]

    if current_pos in small_caves:
        if current_pos not in visted:
            visted[current_pos] = 1
        else:
            visted[current_pos] += 1

            if visted[current_pos] >= 2:
                allow_visting_this_cave = False

    all_paths = []

    for next_cave in map_dict[current_pos]:
        if next_cave != "start":
            new_paths = []

            if next_cave not in path or next_cave.isupper(
            ) or allow_visting_this_cave:
                new_paths = Find_paths(map_dict, next_cave, path, visted,
                                       allow_visting_this_cave)

            if len(new_paths) > 0:
                for new in new_paths:
                    all_paths.append(new)

    if current_pos in visted.keys():
        visted[current_pos] -= 1

    return all_paths


# Adjacent dictionary
graph = dict()
small_caves = set()

for node_one, node_two in raw:
    Add_edge(graph, node_one, node_two)
    Add_edge(graph, node_two, node_one)

    if node_one.islower():
        small_caves.add(node_one)

    if node_two.islower():
        small_caves.add(node_two)

print(len(Find_paths(graph, "start")))
