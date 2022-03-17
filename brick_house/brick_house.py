import sys
import math

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    length = 0

    # Read in the next line and split as 2 float values speed and distance
    line = sys.stdin.readline().rstrip()
    x, y, z = (int(val) for val in line.split(SEPARATOR))

    length = x + (y*5)

    if length < z:
        print("false")
    elif (z % 5) <= x:
        print("true")
    else:
        print("false")
