#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_to_value: dict[str, int] = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        romans: list[str] = list(reversed(s))
        total: int = 0
        prev_value: int = 0

        for roman in romans:
            curr_value: int = symbol_to_value[roman]
            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value
            prev_value: int = curr_value

        return total


# @lc code=end
