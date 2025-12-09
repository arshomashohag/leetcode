# Python3 Solution

class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        if len(start) != len(result):
            return False
        start_removing_X = ""
        result_removing_X = ""
        r_positions = []
        l_positions = []
        for i in range(len(start)):
            if start[i] == 'R':
                r_positions.append(i)
            if start[i] == 'L':
                l_positions.append(i)
            if start[i] != 'X':
                start_removing_X += start[i]
            if result[i] != 'X':
                result_removing_X += result[i]
        if start_removing_X != result_removing_X:
            return False
        
        return True
