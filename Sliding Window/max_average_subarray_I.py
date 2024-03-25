# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

'''
Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000
'''

from output_decorator import output


def average(nums):
    sum = 0
    n = len(nums)
    for num in nums:
        sum += num

    print(sum/n)
    return sum / n


@output
def findMaxAverage(nums, k):
    sum = 0

    for i in range(0, k):
        sum += nums[i]

    max_sum = sum
    start = 0
    end = k

    while end < len(nums):
        sum -= nums[start]
        start += 1
        sum += nums[end]
        end += 1

        if sum > max_sum:
            max_sum = sum

    return max_sum/k


nums = [1, 12, -5, -6, 50, 3]
k = 4
findMaxAverage(nums, k)
