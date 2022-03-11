import sys


SEPARATOR = "|"


cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    ogList = []
    compedList = []
    # Read in the next line and split as 2 float values speed and distance
    line = sys.stdin.readline().rstrip()
    og, comped = (str(val) for val in line.split(SEPARATOR))
    length = 0

    if len(og)==len(comped) and og != comped:
        for i in og:
            ogList.append(i)
        for j in comped:
            compedList.append(j)

        ogList.sort()
        compedList.sort()

        if ogList == compedList:
            print(line, "= ANAGRAM")
        else:
            print(line, "= NOT AN ANAGRAM")

    else:
        print(line, "= NOT AN ANAGRAM")
