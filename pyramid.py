"""
A function that takes an integer as input,
 and prints a pyramid in the following pattern:
"""

def pyramid(n):
    for i in range(1, n+1):
        s = '*' * (2 * i - 1)
        print(s.center(2 * n + 1))

pyramid(1)
pyramid(2)
pyramid(4)
pyramid(50)