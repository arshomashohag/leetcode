# Python3 Solution
from typing import List

class Solution:
    def count_ones(self, nums: List[int]) -> int:
        return sum(1 for x in nums if x == 1)
    def find_subarray_with_gcd_one(self, nums: List[int]) -> int:
        from math import gcd
        n = len(nums)
        min_length = float('inf')
        at_least_one = False
        for i in range(n-1):
            current_gcd = nums[i]
            for j in range(i + 1, n):
                current_gcd = gcd(current_gcd, nums[j])
                if current_gcd == 1:
                    at_least_one = True
                    min_length = min(min_length, j - i + 1)
                    break
        return min_length if at_least_one else -1

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones_count = self.count_ones(nums)
        if ones_count == n:
            return 0
        if ones_count > 0:
            return n - ones_count

        subarray_length = self.find_subarray_with_gcd_one(nums)
        if subarray_length == -1:
            return -1
        return (subarray_length - 1) + (n - 1)
