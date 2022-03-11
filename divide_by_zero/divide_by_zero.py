import sys

def better_round(input_num, decimals = 0):
    name = input_num % (10 ** -decimals)

    if name * (10 ** decimals) >= 5:
        input_num += (10 ** (decimals + 1))
    return input_num - (name)

num_cases = int(sys.stdin.readline().rstrip())

for _ in range(num_cases):
    arr = sys.stdin.readline().rstrip().split(" ")

    dividend = True
    divisor = True

    try:
        arr[0] = float(arr[0])
    except:
        dividend = False

    try:
        arr[1] = float(arr[1])
    except:
        divisor = False

    if not dividend:
        print("Invalid Dividend")
    elif not divisor:
        print("Invalid Divisor")
    elif arr[1] == 0:
        print("Divide by Zero")
    else:
        output = float(arr[0]) / float(arr[1])
        print(better_round(output, 1))