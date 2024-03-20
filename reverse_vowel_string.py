# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

'''
Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
'''

# Similar Questions


def reverseString(string):
    s = [char for char in string]
    reverse = ''
    start = 0
    end = len(s)-1
    while (start < end):
        s[start], s[end] = s[end], s[start]
        start, end = start + 1, end - 1

    for char in s:
        reverse += char

    return reverse


def finalString(s):
    final_string = ""
    for char in s:
        if char == 'i':
            final_string = reverseString(final_string)
        else:
            final_string += char
    return final_string


def sortVowels(s):
    store = []
    string = [char for char in s]
    for i in range(0, len(string)):
        if is_vowel(string[i]):
            store.append(string[i])
            string[i] = '_'

    store.sort()
    index = 0
    for i in range(0, len(string)):
        if string[i] == '_':
            string[i] = store[index]
            index += 1

    result = ''
    for char in string:
        result += char

    return result


# Main Question
def is_vowel(char):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if char.lower() in vowels:
        return True
    else:
        return False


def reverseVowels(s):
    store = []
    string = [char for char in s]
    for i in range(0, len(string)):
        if is_vowel(string[i]):
            store.append(string[i])
            string[i] = '_'

    store = reverseString(store)
    index = 0
    for i in range(0, len(string)):
        if string[i] == '_':
            string[i] = store[index]
            index += 1

    result = ''
    for char in string:
        result += char

    return result


# s = "hello"
# # s = "leetcode"
# result = reverseVowels(s)
# print(result)

s = "leetcode"
result = reverseVowels(s)
print(result)
