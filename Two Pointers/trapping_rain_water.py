# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

'''
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
'''

from output_decorator import output


@output
def trap(height):
    left = [0]*len(height)
    right = [0]*len(height)
    water = 0

    left[0] = height[0]
    for i in range(1, len(height)):
        left[i] = max(height[i], left[i-1])

    right[len(height)-1] = height[len(height)-1]
    for i in range(len(height)-2, -1, -1):
        right[i] = max(height[i], right[i+1])

    for i in range(0, len(height)):
        water += min(left[i], right[i]) - height[i]

    return water


height = [3, 1, 2, 4, 0, 1, 3, 2]
trap(height)
