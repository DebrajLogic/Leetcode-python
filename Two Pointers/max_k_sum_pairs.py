# ou are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.

'''
Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
'''
from output_decorator import output


@output
def maxOperations(nums, k):

    start = 0
    end = len(nums) - 1
    count = 0
    nums.sort()

    while (start < end):
        sum = nums[start] + nums[end]
        if sum == k:
            count += 1
            start += 1
            end -= 1
        elif sum < k:
            start += 1
        else:
            end -= 1

    return count


nums = [1, 2, 3, 4]
k = 5
maxOperations(nums, k)
