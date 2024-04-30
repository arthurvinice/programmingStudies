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
