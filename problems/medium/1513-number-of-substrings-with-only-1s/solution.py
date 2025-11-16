# Python3 Solution

class Solution:
    def numSub(self, s: str) -> int:
        # Your solution here
        result = 0
        count_ones = 0
        for i in range(len(s)):
            if s[i] == '1':
                count_ones += 1
            else:
                result += (count_ones*(count_ones + 1))//2
                count_ones = 0

        if count_ones > 0:
            result += (count_ones*(count_ones + 1))//2
        return result % (10**9 + 7)