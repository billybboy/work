"""
Write a function called "flatten" that flattens an list
"""

def flatten(lst):
    result = []
    for i in lst:
        if type(i) == type([]):
            flatten(i)
        else:
            result.append(i)
    return result

print(flatten([1, [[], 2, [0, [1]], [3]], [1, 3, [3], [4, [1]], [2]]]))