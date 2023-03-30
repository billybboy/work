"""
Write a function called "intersection" that takes 2 lists,
and returns an list of elements that are in the intersection of 2 list.
"""

def intersection(lst_1, lst_2):
    result = []
    for i in lst_1:
        for j in lst_2:
            if i == j:
                result.append(i)
    print(result)

intersection([1, 3, 4, 6, 10], [5, 11, 4, 3, 100, 144, 0])