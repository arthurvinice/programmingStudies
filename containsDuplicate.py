# Given an integer array nums, return true if any value appears at least
# twice in the array, and return false if every element is distinct.
# Challenge available in leetcode.com

def containsDuplicate(nums: list[int]) -> bool:
  test = list(set(nums))  
  if len(test) != len(nums):
    return True
  else:
    return False
