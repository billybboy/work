"""從1-100猜數字"""
import random
num = int(input("please enter a number in 1-100: "))
count = 0 #設定初始猜測次數
target = random.randint(1, 101) #建立1-100隨機數
while num != target:
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

