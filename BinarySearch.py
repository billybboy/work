def binarySearch(arr, num):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if num == arr[mid]:
            return mid
        elif num > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

a = sorted(list(map(int, input().split())))
num = int(input())
print(binarySearch(a, num))