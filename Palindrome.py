# 確認一字串是否為回文
s = input("please enter a word: ")
def isPalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return str + " is not a palindrome"
    return str + "  is a panlindrome"
print(isPalindrome(s))