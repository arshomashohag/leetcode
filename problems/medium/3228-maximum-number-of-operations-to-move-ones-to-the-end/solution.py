# Python3 Solution

class Solution:
    def maxOperations(self, s: str) -> int:
        # Your solution here
        count_ones_by_position = {}
        result = 0
        for i, char in enumerate(s):
            if char == '1':
                count_ones_by_position[i] = count_ones_by_position.get(i - 1, 0) + 1
                if i+1 < len(s) and s[i + 1] == '0':
                    result += count_ones_by_position[i]
            else:
                count_ones_by_position[i] = count_ones_by_position.get(i - 1, 0)

        return result