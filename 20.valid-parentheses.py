#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack: list = []
        open: list[str] = ["(", "{", "["]
        close: list[str] = [")", "}", "]"]
        pairs: dict[str, str] = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in open:
                stack.append(c)
            if c in close:
                if stack:
                    if pairs[c] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        return False if stack else True


# @lc code=end
