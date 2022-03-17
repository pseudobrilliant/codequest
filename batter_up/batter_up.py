import sys

SEPARATOR = ":"

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    totalruns = 0
    totalatbat = 0

    # Read in the next line and split as 2 float values speed and distance
    line = sys.stdin.readline().rstrip()
    x, y = (str(val) for val in line.split(SEPARATOR))

    for i in y:
        if i == "1":
            totalruns += 1
            totalatbat += 1
        elif i == "2":
            totalruns += 2
            totalatbat += 1
        elif i == "3":
            totalruns += 3
            totalatbat += 1
        elif i == "H":
            totalruns += 4
            totalatbat += 1
        elif i == "K":
            totalatbat += 1
        else:
            pass
    if totalatbat > 0:
        total = format(float(totalruns/totalatbat), '.3f')
        print(x,"=",total,sep="")
    else:
        print(x,"=0.000",sep="")
