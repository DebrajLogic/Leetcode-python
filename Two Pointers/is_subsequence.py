# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

'''
Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
'''
from output_decorator import output


@output
def isSubsequence(s, t):
    read_ptr = 0

    for char in t:

        if s[read_ptr] == char:

            read_ptr += 1
            if read_ptr == len(s):
                return True

    return False


s = "acb"
t = "ahbgdc"
isSubsequence(s, t)
