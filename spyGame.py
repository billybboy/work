"""
Write a function that check if a list contains a subsequence of 007
"""

def spyGame(lst):
    s = [0, 0, 7]
    pointer_s = 0
    pointer_lst = 0
    while pointer_lst < len(lst):
        if lst[pointer_lst] == s[pointer_s]:
            pointer_s += 1
            if pointer_s == len(s):
                return True
        pointer_lst += 1
    return False

print(spyGame([1, 2, 4, 0, 3, 0, 7])) # True
print(spyGame([1, 2, 5, 0, 3, 1, 7])) # False