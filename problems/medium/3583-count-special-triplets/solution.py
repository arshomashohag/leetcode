# Python3 Solution
from typing import List

class Solution:
    def __init__(self):
        self.count_from_left = {}
        self.count_from_right = {}
        self.results = []
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        self.results = [0] * n
        for i in range(n):
            num = nums[i]
            double_num = num * 2
            self.results[i] = self.count_from_left.get(double_num, 0)
            self.count_from_left[num] = self.count_from_left.get(num, 0) + 1

        total_triplets = 0
        for i in range(n-1, -1, -1):
            num = nums[i]
            double_num = num * 2
            total_triplets += self.results[i] * self.count_from_right.get(double_num, 0)
            self.count_from_right[num] = self.count_from_right.get(num, 0) + 1
        return total_triplets % (10**9 + 7)