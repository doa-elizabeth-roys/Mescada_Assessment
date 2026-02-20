def is_pallindrome(word):
    word = word.upper()
    if len(word) == 0:
        return None
    elif word == word[::-1]:
        return f"{word} is a pallindrome"
    else:
        return f"{word} is not a pallindrome"
    

print(is_pallindrome("testing"))
print(is_pallindrome(""))
print(is_pallindrome("Noon"))
print(is_pallindrome("racecar"))
