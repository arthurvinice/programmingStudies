# Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.
# You must implement a solution with a linear runtime complexity
# and use only constant extra space.
# Challenge available in leetcode.com

def singleNumber(nums: list[int]) -> int:
        if len(nums) < 0:
            return 0
        else:
            dif = 0
            for num in nums:
                dif ^= num
            return dif
    
print(singleNumber([4,1,2,1,2]))
