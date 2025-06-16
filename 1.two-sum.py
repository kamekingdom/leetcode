#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    # First Commit
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]

    # Second Commit
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_idx = {}
        for idx, num in enumerate(nums):
            complement: int = target - num
            if complement in num_to_idx:
                return [num_to_idx[complement], idx]
            num_to_idx[num] = idx


# @lc code=end
