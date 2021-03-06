# 198. House Robber  QuestionEditorial Solution

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n    = 1,       2,                     3, ...
        # f(n) = nums[0], max{nums[0], nums[1]}, max{f(1)+nums[2], f(2)}, ...
        # f(n) = max(f(n-2)+nums[n-1], f(n-1))
        # Time ~ O(n)
        a = b = 0
        for i in nums:
            a, b = b, max(a+i,b)
        return b
