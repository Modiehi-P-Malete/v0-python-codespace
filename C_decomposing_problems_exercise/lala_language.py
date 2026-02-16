# Write a function `lala_language` that accepts a sentence string as an argument.
# The function should return a new sentence where words longer than 3 characters
# are modified.
#
# Modified words should have each vowel followed by 'l' and the same vowel again.
# See the examples below.

print(lala_language('this is pretty strange'))
# 'thilis is preletty stralangele'

print(lala_language('can you speak our language'))
# 'can you spelealak our lalangulualagele'


def lala_language(sentence):
    words = sentence.split(" ")
    result = []

    for word in words:
        if len(word) > 3:
            new_word = change_vowel(word)
            result.append(new_word)
        else:
            result.append(word)

    return " ".join(result)


def change_vowel(word):
    vowels = "aeiou"
    changed_word = ""

    for char in word:
        if char in vowels:
            changed_word += char + "l" + char
        else:
            changed_word += char

    return changed_word


print(lala_language('this is pretty strange'))
print(lala_language('can you speak our language'))