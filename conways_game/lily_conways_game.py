import sys

num_cases = int(sys.stdin.readline().rstrip())

for _ in range(num_cases):
    gens = int(sys.stdin.readline().rstrip())

    board = []
    buffer = []

    for h in range(10):
        board.append(list(sys.stdin.readline().rstrip()))

    for i in range(10):
        for j in range(10):
            board[i][j] = int(board[i][j])

    for i in range(10):
        for j in range(10):
            print(board[i][j], end = " ")
        print()
    print()
    for h in range(gens):
        buffer = board

        for i in range(10):
            for j in range(10):
                cell_counter = 0
                try:
                    if board[i - 1][j - 1] == 1:
                        cell_counter += 1
                except IndexError:
                    cell_counter += 0
                try:
                    if board[i - 1][j] == 1:
                        cell_counter += 1
                except IndexError:
                    cell_counter += 0
                try:
                    if board[i - 1][j + 1] == 1:
                        cell_counter += 1
                except IndexError:
                    cell_counter += 0
                try:
                    if board[i][j - 1] == 1:
                        cell_counter += 1
                except IndexError:
                    cell_counter += 0
                try:
                    if board[i][j + 1] == 1:
                        cell_counter += 1
                except IndexError:
                    cell_counter += 0
                try:
                    if board[i + 1][j - 1] == 1:
                        cell_counter += 1
                except IndexError:
                    cell_counter += 0
                try:
                    if board[i + 1][j] == 1:
                        cell_counter += 1
                except IndexError:
                    cell_counter += 0
                try:
                    if board[i + 1][j + 1] == 1:
                        cell_counter += 1
                except IndexError:
                    cell_counter += 0

                if board[i][j] == 1:
                    if cell_counter <= 1:
                        buffer[i][j] = 0
                    elif cell_counter == 2 or cell_counter == 3:
                        buffer[i][j] = 1
                    else:
                        buffer[i][j] = 0
                else:
                    if cell_counter == 3:
                        buffer[i][j] = 1

                cell_counter = 0

        board = buffer

        for i in range(10):
            for j in range(10):
                print(board[i][j], end = " ")
            print()
        print()