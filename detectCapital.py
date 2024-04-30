# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

def detectCapitalUse(word: str) -> bool:
    if 1 <= len(word) <= 100:
        if word[0].isupper():
            if len(word) == 1:
                return True
            if word[1:].islower() or word[1:].isupper():
                return True
        elif word[0].islower():
            if len(word) == 1:
                return True
            if word[1:].islower():
                return True
            else:
                return False
        return False
