import sys

Cases = int(sys.stdin.readline().rstrip())

for _ in range(Cases):
    CaseNums = sys.stdin.readline().rstrip().split(" ")
    
    Num1 = CaseNums[0]
    
    Num2 = CaseNums[1]
    
    print((int(Num1) + int(Num2)), (int(Num1) * int(Num2)))