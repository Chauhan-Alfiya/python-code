def vowel(ch):
    if ch in "aeiouAEIOU":
        return True
    else:
        return False

c = input("Enter character: ")
print(vowel(c))