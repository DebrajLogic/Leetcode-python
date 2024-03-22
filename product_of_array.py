# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

'''
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

# Similar Questions


def maxProduct(nums):
    current_product = 1
    max_product = float('-inf')
    for i in range(0, len(nums)):
        current_product *= nums[i]
        max_product = max(current_product, max_product)
        if current_product == 0:
            current_product = 1

    current_product = 1
    for i in range(len(nums)-1, -1, -1):
        current_product *= nums[i]
        max_product = max(current_product, max_product)
        if current_product == 0:
            current_product = 1

    return max_product


def constructProductMatrix(grid):
    rows = len(grid)
    cols = 1
    p = [0 for col in range(cols) for row in range(rows)]

    return p


grid = [[1, 2], [3, 4]]
result = constructProductMatrix(grid)
print(result)
