raw = [i.rstrip() for i in open("./input_testing.txt", "r").readlines()]
start_point = (0, 0)
end_point = (len(raw) - 1, len(raw[len(raw) - 1]) - 1)

print(start_point)
print(end_point)
