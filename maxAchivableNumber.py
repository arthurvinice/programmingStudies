# An integer x is called achievable if it can become equal to num after applying the following operation no more than t times:
# Increase or decrease x by 1, and simultaneously increase or decrease num by 1.
# Return the maximum possible achievable number. 
# It can be proven that there exists at least one achievable number.

# Challenge available in leetcode.com

def theMaximumAchievableX(num: int, t: int) -> int:
    if num >= 1 and t <= 50:
        x = num +(2*t) 
        return x
    else:
        return 0        
