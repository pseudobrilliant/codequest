import sys

num_cases = int(sys.stdin.readline().rstrip())

for _ in range(num_cases):
    num_teams = int(sys.stdin.readline().rstrip())

    total = 0

    for _ in range(num_teams):
        count = int(sys.stdin.readline().rstrip())
        total += count

    print(total)