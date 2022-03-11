import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())


def close(y_pos, x_pos, arr):
    for i in range(-1,2):
        for j in range(-1,2):
            if y_pos+i >= 0 and y_pos+i < rows and x_pos+j >= 0 and x_pos+j < cols:
                if arr[y_pos+i][x_pos+j] != "*":
                    arr[y_pos+i][x_pos+j] += 1
    return arr

for caseNum in range(cases):

    grid = []
    line = sys.stdin.readline().rstrip()
    rows, cols, bombs = (int(val) for val in line.split(SEPARATOR))

    grid = [[0 for _ in range(cols)]for _ in range(rows)]
    for bomb in range(bombs):
        line = sys.stdin.readline().rstrip()
        y, x = (int(val) for val in line.split(SEPARATOR))
        for i in range(rows):
            for j in range(cols):
                if y == i and x == j:
                    grid[i][j] = "*"
                    grid = close(i, j, grid)

    for i in range(rows):
        for j in range(cols):
            print(grid[i][j], end = "")
        print()
        