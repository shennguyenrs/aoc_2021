raw = [i for i in open("input.txt", "r").readlines()][0].rstrip().split(',')

crab_dict = dict()

for i in raw:
    if int(i) in crab_dict.keys():
        crab_dict[int(i)] += 1
    else:
        crab_dict[int(i)] = 1


# Find the fuel cost
def Calcuate_fuel_cost(mean_key, map_dict):
    cost = 0

    for key in map_dict.keys():
        fuel = abs(mean_key - key)
        cost += fuel * map_dict[key]

    return cost


min_cost = Calcuate_fuel_cost(min(crab_dict.keys()), crab_dict)

for key in crab_dict.keys():
    fuel_cost = Calcuate_fuel_cost(key, crab_dict)
    if fuel_cost < min_cost:
        min_cost = fuel_cost

print(min_cost)
