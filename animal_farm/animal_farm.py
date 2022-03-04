import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):

    # Read in the next line and split as 2 float values speed and distance
    line = sys.stdin.readline().rstrip()
    x, y, z = (float(val) for val in line.split(SEPARATOR))

    x = x*2
    y = y*4
    z = z*4

    print(int(x+y+z))