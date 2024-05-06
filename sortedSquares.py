# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.
# Challenge available in leetcode.com

def sortedSquares(nums: list[int]) -> list[int]:
    if 1 <= len(nums) <= 10**4:
        sqrs_array = []
        for i in nums:
            num = i**2
            sqrs_array.append(num)
        sqrs_array.sort()
        return sqrs_array
