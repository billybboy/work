import random

def number(num):
    if num % 2 == 0:
        print("this number is an even.")
    else:
        print("this number is an odd.")

num = random.randint(0, 1000)

print(num)
number(num)