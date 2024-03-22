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

# Main Question


def productExceptSelf(nums):
    left = [0]*len(nums)
    right = [0]*len(nums)
    result = []

    left[0] = 1
    for i in range(1, len(nums)):
        left[i] = left[i-1] * nums[i-1]
        print(f'left[{i}] = {left[i-1]} * {nums[i-1]}')

    right[len(nums)-1] = 1
    for i in range(len(nums)-2, -1, -1):
        right[i] = right[i+1]*nums[i+1]
        print(f'right[{i}] = {right[i+1]} * {nums[i+1]}')

    for i in range(0, len(nums)):
        result.append(left[i]*right[i])

    return result


nums = [1, 2, 3, 4]
result = productExceptSelf(nums)
print(result)
