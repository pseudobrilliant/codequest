import sys

SEPARATOR = ":"

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):

    # Read in the next line and split as 2 float values speed and distance
    line = sys.stdin.readline().rstrip()
    speed, distance = (float(val) for val in line.split(SEPARATOR))

    if speed > 0:
        time = distance / speed
        if time <= 1:
            print("SWERVE")
        elif time <= 5:
            print("BRAKE")
        else:
            print("SAFE")
    else:
        print("SAFE")