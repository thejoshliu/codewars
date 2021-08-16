# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.

def disemvowel(string_):
    string_ = string_.replace('a','')
    string_ = string_.replace('e','')
    string_ = string_.replace('i','')
    string_ = string_.replace('o','')
    string_ = string_.replace('u','')
    string_ = string_.replace('A','')
    string_ = string_.replace('E','')
    string_ = string_.replace('I','')
    string_ = string_.replace('O','')
    string_ = string_.replace('U','')
    return string_