# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'

'''
Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
'''
from output_decorator import output


@output
def maxVowels(s, k):
    vowel = 'aeiou'
    vowels_max = 0
    vowels_count = 0
    for i in range(0, k):
        if s[i] in vowel:
            vowels_count += 1

    vowels_max = vowels_count

    start = 0
    end = k

    while end < len(s):
        if s[start] in vowel:
            vowels_count -= 1

        if s[end] in vowel:
            vowels_count += 1

        start += 1
        end += 1

        if vowels_count > vowels_max:
            vowels_max = vowels_count

    return vowels_max


s = "abciiidef"
k = 3
maxVowels(s, k)
