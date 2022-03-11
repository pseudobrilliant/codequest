import sys

SWERVE_SECONDS = 1
BREAK_SECONDS = 5
SEPARATOR = ":"

num_cases = int(sys.stdin.readline().rstrip())

for _ in range(num_cases):

    # Read in the next line and split as 2 float values speed and distance
    line = sys.stdin.readline().rstrip()
    arr = line.split(SEPARATOR)
    speed, distance = (float(val) for val in arr)

    # Check whether current vehicle will cover the current distance within each SECONDS range
    if speed * SWERVE_SECONDS >= distance:
        print("SWERVE")
    elif speed * BREAK_SECONDS >= distance:
        print("BRAKE")
    else:
        print("SAFE")
