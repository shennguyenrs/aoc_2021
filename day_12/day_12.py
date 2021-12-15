raw = [i.rstrip().split("-") for i in open("input_testing.txt", "r")]


def Add_edge(graph_dict, key, value):
    if key not in graph_dict.keys():
        graph_dict[key] = [value]
    else:
        graph_dict[key].append(value)


def Find_paths(graph_dict, start_node, end_node, path=[]):
    path = path + [start_node]

    if start_node == end_node:
        return [path]

    paths = []

    for node in graph_dict[start_node]:
        new_paths = []

        if node not in path or (node in path and node.isupper()):
            new_paths = Find_paths(graph_dict, node, end_node, path)

        if len(new_paths) > 0:
            for new_path in new_paths:
                paths.append(new_path)

    return paths


# Adjacent dictionary
graph = dict()
start_end_nodes = ["start", "end"]
small_caves = set()

for node_one, node_two in raw:
    Add_edge(graph, node_one, node_two)
    Add_edge(graph, node_two, node_one)
    small_caves.add(node_one)
    small_caves.add(node_two)

all_paths = Find_paths(graph, "start", "end")

print(len(all_paths))
