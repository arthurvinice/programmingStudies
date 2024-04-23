# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Challenge available in leetcode.com

def strStr(haystack: str, needle: str) -> int:
    haystack.lower().find(needle)
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1
        