# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed.
# Then return the number of elements in nums which are not equal to val.
# Challenge available in leetcode.com

def removeElement(nums: list[int], val: int) -> int:
    i = 0
    nums.sort()
    while i < len(nums):
        if nums[i] == val:
            nums.remove(nums[i])
        else:
            i += 1
    return len(nums)
