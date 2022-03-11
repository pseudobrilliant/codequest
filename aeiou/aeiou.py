import sys

SEPARATOR = " "
AEIOU = 0

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):

    # Read in the next line and split as 2 float values speed and distance
    line = sys.stdin.readline().rstrip()
    for letters in line:
        if letters in ('a','e','i','o','u'):
            AEIOU += 1


    
    print(AEIOU)
    AEIOU = 0