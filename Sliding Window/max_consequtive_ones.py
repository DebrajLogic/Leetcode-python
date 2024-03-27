# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

'''
Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
'''
from output_decorator import output


@output
def longestOnes(nums, k):
    zeros = 0
    start_ptr = 0
    max_length = 0

    for end_ptr in range(0, len(nums)):
        if nums[end_ptr] == 0:
            zeros += 1

        while zeros > k:
            if nums[start_ptr] == 0:
                zeros -= 1

            start_ptr += 1

        max_length = max(max_length, end_ptr - start_ptr + 1)

    return max_length


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
longestOnes(nums, k)
