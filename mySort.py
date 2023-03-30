"""
A function that takes an list of integers as input,
and returns the sorted version of the input list.
You are not allowed to use the built-in sorted() function.
"""

def mySort(lst):
    result = []
    while len(lst) > 0:
        min_ele = lst[0]
        for i in lst:
            if i < min_ele:
                min_ele = i
        result.append(min_ele)
        lst.remove(min_ele)
    print(result)

mySort([17, 0, -3, 2, 1, 0.5])

