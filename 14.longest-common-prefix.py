#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix: str = strs[0]
        for target_str in strs[1:]:
            same_str: str = ""
            for idx in range(min(len(target_str), len(prefix))):
                if target_str[idx] == prefix[idx]:
                    same_str += prefix[idx]
                else:
                    break
            prefix = same_str

        return prefix


# @lc code=end
