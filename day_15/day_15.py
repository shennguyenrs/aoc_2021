import heapq

raw = [i.rstrip() for i in open("./input.txt", "r").readlines()]


def Dijkstras_Find_shortest_path(
    start: tuple[int, int], end: tuple[int, int], weight_map: list[list[int]]
) -> tuple[dict[tuple[int, int], tuple[int, int]], dict[tuple[int, int], int]]:
    priority_queue = []
    cost_to_node = dict()
    visited_points = set()
    prev_from_node = dict()

    max_x = end[0]
    max_y = end[1]

    heapq.heapify(priority_queue)

    # Push the start to queue

    heapq.heappush(priority_queue, (0, start))

    # Cost to travel to the starting point is 0
    # and other point is inf
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            cost_to_node[(x, y)] = float('inf')

    cost_to_node[start] = 0

    # Find the shortest path
    while len(priority_queue) > 0:
        _, current_node = heapq.heappop(priority_queue)

        # Add current node to visted
        visited_points.add(current_node)

        # Stop when meet end point
        if current_node == end:
            break

        # Add next nodes
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if max_x >= current_node[0] + x >= 0 and max_y >= current_node[
                    1] + y >= 0:
                neighbor_node = (current_node[0] + x, current_node[1] + y)
                distance = weight_map[neighbor_node[1]][neighbor_node[0]]

                if neighbor_node not in visited_points:
                    old_cost = cost_to_node[neighbor_node]
                    new_cost = cost_to_node[current_node] + distance

                    if new_cost < old_cost:
                        heapq.heappush(priority_queue,
                                       (new_cost, neighbor_node))
                        cost_to_node[neighbor_node] = new_cost
                        prev_from_node[neighbor_node] = current_node

    return prev_from_node, cost_to_node


# Construct the shortest path
def Print_map(prev_from_node: dict[tuple[int, int], tuple[int, int]],
              start: tuple[int, int], end: tuple[int, int]) -> None:
    path = []
    shortest_path = []

    path.append(prev_from_node[end])
    shortest_path.append(end)
    shortest_path.append(prev_from_node[end])

    max_x = end[0]
    max_y = end[1]

    while len(path) > 0:
        current_node = path.pop()

        if current_node == start:
            break

        path.append(prev_from_node[current_node])
        shortest_path.append(prev_from_node[current_node])

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in shortest_path:
                print("x", end="")
            else:
                print("_", end="")

        print()


def Expand_map(initial_map: list[list[int]]) -> list:
    expand_times = 5
    expanded_maps = [[[] for _ in range(expand_times)]
                     for _ in range(expand_times)]
    expanded_maps[0][0] = initial_map

    # Expand map with expanded times
    for expanded_line in range(expand_times):
        for expanded_row in range(expand_times):
            if (expanded_row, expanded_line) == (0, 0): continue

            new_map = []

            if expanded_row == 0:
                ref_line = 0 if expanded_line == 0 else expanded_line - 1
                ref_row = expanded_row
            else:
                ref_line = expanded_line
                ref_row = expanded_row - 1

            for line in expanded_maps[ref_line][ref_row]:
                new_map.append(
                    list(map(lambda x: x + 1 if x != 9 else 1, line)))

            expanded_maps[expanded_line][expanded_row] = new_map

    # Join children map
    joined_expanded_map = []

    for line_maps in expanded_maps:
        for i in range(len(line_maps[0])):
            temp_line = []

            for j in range(expand_times):
                temp_line += line_maps[j][i]

            joined_expanded_map.append(temp_line)

    return joined_expanded_map


def Part_One(data: list[str]) -> None:
    weight_graph = []

    for line in data:
        weight_graph.append(list(map(int, list(i for i in line))))

    start_point = (0, 0)
    end_point = (len(data[0]) - 1, len(data) - 1)

    _, cost_dict = Dijkstras_Find_shortest_path(start_point, end_point,
                                                weight_graph)

    print(cost_dict[end_point])


def Part_Two(data: list[str]) -> None:
    weight_graph = []

    for line in data:
        weight_graph.append(list(map(int, list(i for i in line))))

    expanded_weighted_graph = Expand_map(weight_graph)

    start_point = (0, 0)
    end_point = (len(expanded_weighted_graph[0]) - 1,
                 len(expanded_weighted_graph) - 1)

    _, cost_dict = Dijkstras_Find_shortest_path(start_point, end_point,
                                                expanded_weighted_graph)

    print(cost_dict[end_point])


Part_Two(raw)
