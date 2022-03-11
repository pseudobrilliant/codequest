import sys
import math

def better_round(input_var, decimals = 0):
    input_num = input_var

    if input_num != 0:
        if input_num > 0:
            input_num += (0.5 * (10 ** -decimals))
        elif input < 0:
            input_num -= (0.5 * (10 ** -decimals))
    
        input_num *= 10 ** decimals

        input_num = math.floor(input_num)

        input_num /= 10 ** decimals

    return input_num

num_cases = int(sys.stdin.readline().rstrip())

for _ in range(num_cases):
    arr = sys.stdin.readline().rstrip().split(" ")

    dividend = True
    divisor = True
    divide = True

    try:
        arr[0] = float(arr[0])
    except:
        dividend = False

    try:
        arr[1] = float(arr[1])
    except:
        divisor = False
    
    try:
        output = float(arr[0]) / float(arr[1])
    except:
        divide = False


    if not dividend:
        print("Invalid Dividend")
    elif not divisor:
        print("Invalid Divisor")
    elif not divide:
        print("Divide By Zero") 
    else:
        print(better_round(output, 1))