raw = [i for i in open("input.txt", "r").readlines()][0].rstrip().split(',')

crab_dict = dict()
sorted_raw = sorted(map(int, raw))

for i in raw:
    if int(i) in crab_dict.keys():
        crab_dict[int(i)] += 1
    else:
        crab_dict[int(i)] = 1


# Find the fuel cost
def Part_one_cost(mean_key, map_dict):
    cost = 0

    for key in map_dict.keys():
        fuel = abs(mean_key - key)
        cost += fuel * map_dict[key]

    return cost


def Part_two_cost(mean_key, map_dict):
    cost = 0
    for key in map_dict.keys():
        fuel = abs(mean_key - key) * (abs(mean_key - key) + 1) / 2
        cost += fuel * map_dict[key]

    return cost


def Find_median(sorted_list):
    median_pos = len(sorted_list) // 2
    return sorted_list[median_pos]


def Find_averange(a_list):
    return sum(a_list) // len(a_list)


print(Part_one_cost(Find_median(sorted_raw), crab_dict))
print(Part_two_cost(Find_averange(sorted_raw), crab_dict))
