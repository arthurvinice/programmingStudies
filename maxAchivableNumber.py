# Challenge available in leetcode.com

def theMaximumAchievableX(num: int, t: int) -> int:
    if num >= 1 and t <= 50:
        x = num +(2*t) 
        return x
    else:
        return 0        
