# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

'''
Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""
'''


def findGCD(nums):
    a = min(nums)
    b = max(nums)
    gcd = 1

    for i in range(1, b):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd


def smallestEvenMultiple(n):
    if n % 2 != 0:
        multiple = 2 * n
    else:
        for i in range(1, 2 * n):
            if (n * i) % 2 == 0:
                multiple = n * i
                break
    return multiple


def gcdOfStrings(str1, str2):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    len_gcd = gcd(len(str1), len(str2))
    sub_string = str1[:len_gcd]
    if str1 + str2 == str2 + str1 and sub_string * (len(str1)//len_gcd) == str1 and sub_string * (len(str2)//len_gcd) == str2:
        return sub_string
    else:
        return ""


str1 = "ABABAB"
str2 = "ABAB"
nums = [2, 5, 6, 9, 10]

gcd = gcdOfStrings(str1, str2)
print(gcd)
