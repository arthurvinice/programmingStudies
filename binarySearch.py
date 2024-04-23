#My Python version of Binary Search Algorithm

def binarySearch(arr: list[int], num: int):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right)//2
        if arr[mid] == num:
            return arr[mid]
        elif arr[mid] < num:
            left += 1
        else:
            right -= 1
    return "Not Found"
