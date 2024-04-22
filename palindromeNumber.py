# Given an integer x, return true if x is a 
# palindrome, and false otherwise.
# Challenge available in leetcode.com

def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        if x_str[0] == '-':
            return False
        
        l = 0
        r = len(x_str) - 1
        
        while l < r:
            if x_str[r] != x_str[l]:
                return False
            l += 1
            r -= 1
        return True
