raw = list(
    filter(lambda x: x != ",",
           [i for i in open("input.txt", "r").readline().rstrip()]))

keys = [i for i in range(9)]
values = [0] * 9

fish_dict = dict(zip(keys, values))

# Input range
days = int(input("Enter the day to calculate the total fish? "))

for i in raw:
    fish_dict[int(i)] += 1

# Calculate fish in range
for _ in range(days):
    temp_dict = dict(zip(keys, values))

    for key in fish_dict.keys():
        if key == 0:
            temp_dict[8] += fish_dict[0]
            temp_dict[6] += fish_dict[0]
        else:
            temp_dict[key - 1] += fish_dict[key]

    fish_dict = temp_dict

total_fish = sum([i for i in fish_dict.values()])
print(total_fish)
