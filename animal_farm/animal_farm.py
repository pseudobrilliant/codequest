import sys

num_cases = int(sys.stdin.readline().rstrip())

for _ in range(num_cases):
    arr = sys.stdin.readline().rstrip().split(" ")
    print((int(arr[0]) * 2) + (int(arr[1]) * 4) + (int(arr[2]) * 4))