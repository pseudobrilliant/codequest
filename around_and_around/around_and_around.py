import sys
import math

cases = int(sys.stdin.readline().rstrip())


for caseNum in range(cases):

    # Read in the next line and split as 2 float values speed and distance
    line = sys.stdin.readline().rstrip()
    radius = ((40075/math.pi)/2) + int(line)
    rad = (radius*2)*math.pi
    print(round(rad,1))