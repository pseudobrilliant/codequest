import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())


for _ in range(cases):

    # Read in the next line and split as 2 float values speed and distance
    line = sys.stdin.readline().rstrip()
    x, y = (float(val) for val in line.split(SEPARATOR))

