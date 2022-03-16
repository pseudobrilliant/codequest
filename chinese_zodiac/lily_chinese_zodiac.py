import sys

num_cases = int(sys.stdin.readline().rstrip())

elements = ["Wood", "Fire", "Earth", "Metal", "Water"]
animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]

for _ in range(num_cases):
    year = int(sys.stdin.readline().rstrip())

    if year % 2 == 0:
        first = "Yang"
    else:
        first = "Yin"

    second = elements[((year - 4) % 10) // 2]

    third = animals[(year - 4) % 12]

    print(year, first, second, third)