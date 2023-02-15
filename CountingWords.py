"""計算一段文字的字數"""

words = input("please input some words: ")
list = words.split()
count = len(list)
print("the number of words is " + str(count))
