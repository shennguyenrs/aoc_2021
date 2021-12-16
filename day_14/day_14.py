from math import ceil

raw = [i.rstrip() for i in open("./input.txt", "r").readlines()]

original_string = raw[0]
pair_insertion_dict = dict()

for line in raw[2:]:
    key, value = line.split(" -> ")
    pair_insertion_dict[key] = value


def Middle_insertion(str_pair: str, pair_index: int, map_dict: dict) -> str:
    if pair_index != 0: return map_dict[str_pair] + str_pair[1]
    return str_pair[0] + map_dict[str_pair] + str_pair[1]


def Middle_insertion_list(str_pair: str, map_dict: dict) -> list:
    return [str_pair[0] + map_dict[str_pair], map_dict[str_pair] + str_pair[1]]


def Get_new_str_list(str_to_parse: str) -> list:
    temp = []

    for i in range(len(str_to_parse) - 1):
        temp.append(str_to_parse[i:i + 2])

    return temp


def Part_One(temp_str: str, map_dict: dict) -> int:
    for _ in range(10):
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


def Part_Two(temp_str: str, map_dict: dict) -> None:
    keys_dict = dict()
    key_str_list = Get_new_str_list(temp_str)

    for i in key_str_list:
        if i in keys_dict:
            keys_dict[i] += 1
        else:
            keys_dict[i] = 1

    for _ in range(40):
        temp_dict = dict()

        for parent in keys_dict.keys():
            results = Middle_insertion_list(parent, map_dict)

            # The number of generated children is equal to the number of parent
            # If there are 2 of "NN" in the parent
            # It will become 2 for each "NC" and "CN" with "C" is inserted
            for child in results:
                if child not in temp_dict:
                    temp_dict[child] = keys_dict[parent]
                else:
                    temp_dict[child] += keys_dict[parent]

        keys_dict = temp_dict

    counting_char_dict = dict()

    for parent in keys_dict.keys():
        for char in parent:
            if char in counting_char_dict:
                counting_char_dict[char] += keys_dict[parent]
            else:
                counting_char_dict[char] = keys_dict[parent]

    # By spliting the words in the beginning the total of the characters in the middle of string will be double
    # "NNCB" now becomes "NN", "NC", "CB"
    # However, the amount of first and end is still equal to 1
    max_value = max(counting_char_dict.values())
    min_value = min(counting_char_dict.values())

    print(max_value)
    print(min_value)

    print(ceil((max_value - min_value) / 2))


# print(Part_One(original_string, pair_insertion_dict))
Part_Two(original_string, pair_insertion_dict)
