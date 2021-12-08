# Digits:
#   0: abcefg
#   1: cf
#   2: acdeg
#   3: adcfg
#   4: bcdf
#   5: abdfg
#   6: abdefg
#   7: acf
#   8: abcdefg
#   9: abcdfg

raw = [i.rstrip() for i in open("input.txt", "r").readlines()]
after = [i.split("|")[1].lstrip() for i in raw]
before = [i.split("|")[0].rstrip() for i in raw]


def Part_one(data):
    length_of_digits = [2, 4, 3, 7]  # 1, 4, 7, 8
    counter = 0
    for all in data:
        for pattern in all.split(" "):
            if len(pattern) in length_of_digits:
                counter += 1

    return counter


def Part_Two(encode, decode):
    map_dict = dict()

    # Detect 1, 4, 7, 8
    for chars in encode.split(" "):
        if len(chars) == 2: map_dict[1] = set(chars)
        if len(chars) == 3: map_dict[7] = set(chars)
        if len(chars) == 4: map_dict[4] = set(chars)
        if len(chars) == 7: map_dict[8] = set(chars)

    # Detect others
    for chars in encode.split(" "):
        if set(chars) not in map_dict.values():
            chars_set = set(chars)
            seven_set = set(map_dict[7])
            four_set = set(map_dict[4])

            if len(chars) == 6:
                if len(chars_set.intersection(seven_set)) == 2:
                    map_dict[6] = set(chars)
                elif len(chars_set.intersection(four_set)) == 4:
                    map_dict[9] = set(chars)
                else:
                    map_dict[0] = set(chars)
            else:
                if len(chars_set.intersection(seven_set)) == 3:
                    map_dict[3] = set(chars)
                elif len(chars_set.intersection(four_set)) == 3:
                    map_dict[5] = set(chars)
                else:
                    map_dict[2] = set(chars)

    message = ""
    value_list = list(map_dict.values())
    key_list = list(map_dict.keys())

    for i in decode.split(" "):
        index = value_list.index(set(i))
        message += str(key_list[index])

    return int(message)


counter = 0

for i in range(len(raw)):
    counter += Part_Two(before[i], after[i])

print(counter)
