"""
A function that takes an list as input,
and returns the minimum element in the input list.
"""

def findMin(l):
    if len(l) == 0:
        print('undefined')
    else:
        min_ele = l[0]
        for ele in l:
            if ele < min_ele:
                min_ele = ele
        print(min_ele)


findMin([1, 2, 5, 6, 99, 4, 5]) # returns 1
findMin([]) # returns undefined
findMin([1, 6, 0, 33, 44, 88, -10])