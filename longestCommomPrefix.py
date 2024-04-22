# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Challenge available in leetcode.com

def longestCommonPrefix(strs: list[str]) -> str:
    prefix = ""
    strs = sorted(strs)
    l = strs[0]
    r = strs[-1]
    for i in range(min(len(l), len(r))):
        if l[i] != r[i]:
            return prefix
        prefix += l[i]
    return prefix
    
        
