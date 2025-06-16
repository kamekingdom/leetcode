#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_number: str = str(x)[::-1]
        return str(x) == reversed_number


# @lc code=end
