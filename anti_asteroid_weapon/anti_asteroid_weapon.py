import sys
import math

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    cords = []
    distance = []
    cases2 = int(sys.stdin.readline().rstrip())
    for i in range(cases2):
        line = sys.stdin.readline().rstrip()
        x,y = (float(val) for val in line.split(SEPARATOR))
        dist = math.sqrt(x**2 + y**2)
        distance.append(dist)
        cords.append(line)

    for j in range(len(distance)):
        for i in range(len(distance)):
            if distance[i]>distance[j]:
                temp = distance[i]
                temp2 = cords[i]
                distance[i] = distance[j]
                cords[i] = cords[j]
                distance[j] = temp
                cords[j] = temp2

    for i in range(len(distance)):
        print(cords[i])