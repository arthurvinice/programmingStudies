# Challenge available in leetcode.com
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed.
# Then return the number of elements in nums which are not equal to val.

def removeElement(self, nums: List[int], val: int) -> int:
        i = len(nums)-1
        while i > 0:
            if nums[i] == val:
                nums.pop(i)
            i-=1
        return len(nums)
