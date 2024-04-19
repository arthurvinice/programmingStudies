# Given two strings s and t, return true if t 
# is an anagram of s, and false otherwise.
# Challenge available in leetcode.com

def isAnagram(s: str, t: str) -> bool:
    arrs = []
    for char in s:
        arrs.append(char)
    arrt = []
    for char in t:
        arrt.append(char)
    arrs.sort()    
    arrt.sort()    
    if arrs == arrt:
        return True
    else:
        return False
    
