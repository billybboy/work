"""
Given a list of ints, return True if the list contains a 3 next to a 3.
"""

def has_33(lst):
    if lst == []:
        return False
    i = 0
    while i <= len(lst) - 1:
        if lst[i] == 3 and lst[i+1] == 3:
            return True
        else:
            i += 1
    return False


print(has_33([1, 5, 7, 3, 3])) # True
print(has_33([])) # False
print(has_33([4, 3, 2, 1, 0])) # False