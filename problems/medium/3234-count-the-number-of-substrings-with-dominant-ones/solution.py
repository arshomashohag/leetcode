# Python3 Solution

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Your solution here
        s_len = len(s)
        zero_counts = [0] * (s_len + 1)
        ones_counts = [0] * (s_len + 1)
        for i in range(1, s_len):
            zero_counts[i + 1] = zero_counts[i] + (1 if s[i] == '0' else 0)
            ones_counts[i + 1] = ones_counts[i] + (1 if s[i] == '1' else 0)
        
        result = 0

        for i in range(s_len):
            j = i
            while j < s_len:
                n_zeros = zero_counts[j] - zero_counts[i] + (1 if s[j] == '0' else 0)
                n_ones = ones_counts[j] - ones_counts[i] + (1 if s[j] == '1' else 0)
                if n_ones >= n_zeros**2:
                    result += 1
                    j += 1
                    continue
        
        pass
