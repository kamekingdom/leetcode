#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        stack: list[int] = []
        count: int = 0
        for num in nums:
            if not stack or stack[-1] != num:
                count += 1
                stack.append(num)
            else:
                continue

        for i in range(len(stack)):
            nums[i] = stack[i]

        return count


# @lc code=end
