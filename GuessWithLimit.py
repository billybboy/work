"""從1-100猜數字"""
import random
num = int(input("please enter a number in 1-100: "))
count = 0 #設定初始猜測次數
count_limit = 6
target = random.randint(1, 101) #建立1-100隨機數
while num != target and count <= count_limit:
    if num < 1 or num > 100:
        print("this number is out of range")
        break
    if num > target:
        print("too high")
        num = int(input("please enter another number in 1-100: "))
        count += 1
    if num < target:
        print("too low")
        num = int(input("please enter another number in 1-100: "))
        count += 1
    if num == target:
        print("bingo!")
        print("guess count: " + str(count))
if count > count_limit:
    print("sorry you lose")