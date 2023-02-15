try:
    num = int(input("please enter a number between 1-1000 : "))
    if num < 1 or num > 1000:
         print("this number is out of range")
    else:
        if num % 2 == 0:
            print("this number is an even.")
        else:
            print("this number is an odd.")
except ValueError:
    print("this number is out of range")