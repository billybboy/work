"""輸入一段文字並回傳縮寫"""

words = input("please enter a full meaning of an organization of concept: ")
list = words.split()
acronym = ""
for i in list:
    j = iter(i)
    acronym = acronym + next(j)
print("the acronym of your input is " + acronym)