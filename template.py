import  sys

# Read in the number of use cases present in stdin file
num_cases = int(sys.stdin.readline().rstrip())

# Iterate through each number in case and read expected line
for _ in range(num_cases):
    line = sys.stdin.readline().rstrip()
