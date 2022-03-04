import sys

def fibo(current_position):
    '''Recursive fibonacci function'''
    if current_position < 2:
        return 1
    return fibo(current_position - 1) + fibo(current_position)

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = int(sys.stdin.readline().rstrip())
    i = 0
    while True:
        if fibo(i) == line:
            print("TRUE")
            break
    
        