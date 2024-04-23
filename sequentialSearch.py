#My Python version of Sequential Search algorithm

def sequentialSearch(arr: list[int], num: int):
    arr.sort()
    n = len(arr)
    for i in range(n):
        if arr[i] == num:
            return arr[i]
    return "Not Found"
