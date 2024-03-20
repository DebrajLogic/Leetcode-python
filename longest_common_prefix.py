# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
'''
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''


def longestCommonPrefix(strs):
    if not strs:
        return ''

    prefix = strs[0]

    for string in strs[1:]:
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]

        if not prefix:
            return ""
    return prefix


strs = ["flower", "flow", "flight"]
prefix = longestCommonPrefix(strs)
print(prefix)
