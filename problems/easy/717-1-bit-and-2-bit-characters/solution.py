# Python3 Solution
from operator import index
from typing import List

class Solution:
    def __init__(self):
        self.path_map = {}
        self.bits = None
        self.n = None

    def traverse_bits(self, index: int) -> bool:
        if index == self.n-1 and self.bits[index] == 0:
            return True
        
        if self.bits[index] == 1:
            if index + 2 < self.n:
                return self.traverse_bits(index + 2)
            else:
                return False
        else:
            if index + 1 < self.n:
                return self.traverse_bits(index + 1)
        

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        self.bits = bits
        self.n = len(bits)
        if self.bits[-1] == 1:
            return False
        if self.bits[-1] == 0 and self.n == 1:
            return True
        if self.bits[-1] == 0 and self.bits[-2] == 0:
            return True
        return self.traverse_bits(0)