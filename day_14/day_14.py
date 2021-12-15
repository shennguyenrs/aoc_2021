raw = [i.rstrip() for i in open("./input_testing.txt", "r").readlines()]

original_string = raw[0]
pair_insertion_dict = dict()

for line in raw[2:]:
    key, value = line.split(" -> ")
    pair_insertion_dict[key] = value


def Middle_insertion(str_pair: str, pair_index: int, map_dict: dict) -> str:
    if pair_index != 0: return map_dict[str_pair] + str_pair[1]
    return str_pair[0] + map_dict[str_pair] + str_pair[1]


def Get_new_str_list(str_to_parse: str) -> list:
    temp = []

    for i in range(len(str_to_parse) - 1):
        temp.append(str_to_parse[i:i + 2])

    return temp


def Part_One(temp_str: str, map_dict: dict) -> int:
    for _ in range(40):
        key_str_list = Get_new_str_list(temp_str)
        new_string = ""

        for index in range(len(key_str_list)):
            new_string += Middle_insertion(key_str_list[index], index,
                                           map_dict)

        temp_str = new_string

    occur_dict = dict()

    for char in temp_str:
        if char in occur_dict:
            occur_dict[char] += 1
        else:
            occur_dict[char] = 1

    occur_values = list(occur_dict.values())

    return max(occur_values) - min(occur_values)


print(Part_One(original_string, pair_insertion_dict))
