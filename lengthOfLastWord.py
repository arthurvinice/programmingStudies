# Given a string s consisting of words and spaces, 
# return the length of the last word in the string.
# A word is a maximal substring
# consisting of non-space characters only.
# Challenge available in leetcode.com

def lengthOfLastWord(s: str) -> int:
    words = s.split()
    last = words[-1]
    return print(last)
    
