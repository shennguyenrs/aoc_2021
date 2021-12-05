numbers_to_draw = []
boards = []
row = 5
col = 5

with open("input.txt", "r") as input:
    raw = input.readlines()
    raw_numbers = raw[0].rstrip().split(",")
    raw_boards = raw[2:]

    numbers_to_draw = list(map(lambda x: int(x), raw_numbers))

    i = 0
    while i < len(raw_boards):
        board = []

        if raw_boards[i].rstrip() != "":

            for j in range(col):
                if i + j >= len(raw_boards): break
                line = raw_boards[i + j].rstrip().split()
                converted_line = list(map(lambda x: int(x), line))
                board.append(converted_line)

            boards.append(board)
            i += row
        else:
            i += 1


def Check_row(board):
    for line in board:
        if sum(line) == -5:
            return True

    return False


def Check_col(board):
    sum = 0
    for i in range(col):
        for line in board:
            sum += line[i]

        if sum == -5: return True

    return False


def Sum_board(board):
    total = 0
    for line in board:
        for i in line:
            if i != -1: total += i

    return total


def Bingo_first(data, calling_numbers):
    for value in calling_numbers:
        break_loop = False

        # Mark value to -1 when it is called
        for board in data:
            for line in board:
                for i in range(col):
                    if line[i] == value:
                        line[i] = -1

            if Check_col(board) or Check_row(board):
                print("Bingo")
                print("Score:", Sum_board(board) * value)
                break_loop = True
                break

        if break_loop: break


def Bingo_last(data, calling_numbers):
    bingo_index = []

    for value in calling_numbers:
        break_loop = False

        # Mark value to -1 when it is called
        for index in range(len(data)):
            board = data[index]

            for line in board:
                for i in range(col):
                    if line[i] == value:
                        line[i] = -1

            if Check_col(board) or Check_row(board):
                if index not in bingo_index:
                    bingo_index.append(index)

            if len(bingo_index) == len(data):
                print("Bingo last")
                print("Score:", Sum_board(board) * value)
                break_loop = True
                break

        if break_loop: break


Bingo_last(boards, numbers_to_draw)
