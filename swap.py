"""
A function that takes a string as input,
and returns a new string with lowercase changed to uppercase,
uppercase changed to lowercase
"""

def swap(s):
    result = ''
    for i in s:
        if i.islower():
            result += i.upper()
        else:
            result += i.lower()
    print(result)

swap("Aloha") # returns "aLOHA"
swap("Love you.")