import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):

    # Read in the next line and split as 2 float values speed and distance
    line = sys.stdin.readline().rstrip()
    x, y = (float(val) for val in line.split(SEPARATOR))

    print(int(x+y), end = "")
    print(" ", end = "")
    print(int(x*y))