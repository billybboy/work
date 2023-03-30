"""
Write a function called "inversePyramid" that draws pyramid upside down.
"""

def inversePyramid(n):
    for i in range(n, 0, -1):
        s = '*' * (2 * i - 1)
        print(s.center(2 * n - 1))

inversePyramid(4)
inversePyramid(40)