import math

raw = [i.rstrip() for i in open("input.txt", "r").readlines()]

score_one = {")": 3, "]": 57, "}": 1197, ">": 25137}
score_two = {")": 1, "]": 2, "}": 3, ">": 4}
opennings = ["(", "[", "{", "<"]
closings = [")", "]", "}", ">"]


def Part_one(data):
    error_score = 0
    corrupted_lines = []

    for line in data:
        open_stack = []
        expect_queue = []
        line_length = len(line)

        for chuck in line:
            if len(open_stack) <= line_length // 2:
                if chuck in opennings:
                    open_stack.append(chuck)
                    expect_queue.append(closings[opennings.index(chuck)])
                else:
                    if chuck == expect_queue[len(expect_queue) - 1]:
                        open_stack.pop()
                        expect_queue.pop()
                    else:
                        error_score += score_one[chuck]
                        corrupted_lines.append(line)
                        break
            else:
                error_score += score_one[chuck]
                corrupted_lines.append(line)
                break

    return [corrupted_lines, error_score]


def Part_two(data):
    fixing_scores = []

    for line in data:
        open_stack = []
        expect_queue = []

        for chuck in line:
            if chuck in opennings:
                open_stack.append(chuck)
                expect_queue.append(closings[opennings.index(chuck)])
            else:
                if chuck == expect_queue[len(expect_queue) - 1]:
                    open_stack.pop()
                    expect_queue.pop()

        score = 0

        if len(expect_queue) > 0:
            for i in range(len(expect_queue) - 1, -1, -1):
                score = score * 5 + score_two[expect_queue[i]]

            fixing_scores.append(score)

    return fixing_scores


corrupted, score = Part_one(raw)

incomplete_lines = filter(lambda x: x not in corrupted, raw)
scores = Part_two(incomplete_lines)
sorted_scores = sorted(scores)

print(sorted_scores[math.ceil(len(scores) / 2) - 1])
