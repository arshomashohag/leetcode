# 1513. Number of Substrings With Only 1s

**Difficulty:** Medium  
**Date:** November 16, 2025 (Daily Challenge)  
**Topics:** Math, String  
**Acceptance Rate:** 50.0%

## Problem Description

Given a binary string `s`, return the number of substrings with all characters `1`'s. Since the answer may be too large, return it modulo `10^9 + 7`.

### Example 1:
```
Input: s = "0110111"
Output: 9
Explanation: There are 9 substrings with only 1's characters.
"1" appears 5 times.
"11" appears 3 times.
"111" appears 1 time.
```

### Example 2:
```
Input: s = "101"
Output: 2
Explanation: Substring "1" appears 2 times.
```

### Example 3:
```
Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.
```

### Constraints:
- `1 <= s.length <= 10^5`
- `s[i]` is either `'0'` or `'1'`

---

## Approach & Algorithm

### Key Insight

For a string of consecutive 1's with length `k`, the number of substrings containing only 1's follows a mathematical pattern:

**Formula:** `k × (k + 1) / 2`

This is because:
- Starting at position 0: k substrings
- Starting at position 1: k-1 substrings
- Starting at position 2: k-2 substrings
- ...
- Starting at position k-1: 1 substring

**Total:** 1 + 2 + 3 + ... + k = k × (k + 1) / 2

### Algorithm

1. **Iterate through the string** character by character
2. **Count consecutive 1's** in a variable `count_ones`
3. **When encountering a '0':**
   - Apply the formula to the current segment: `count_ones × (count_ones + 1) / 2`
   - Add the result to the total
   - Reset `count_ones` to 0
4. **After the loop ends:**
   - If there are remaining 1's (string ends with 1's), apply the formula one more time
5. **Return result modulo 10^9 + 7** as required

### Example Walkthrough

```
s = "0110111"

i=0: '0' → count_ones=0, result=0
i=1: '1' → count_ones=1
i=2: '1' → count_ones=2
i=3: '0' → Add 2×3/2=3, reset count_ones=0, result=3
i=4: '1' → count_ones=1
i=5: '1' → count_ones=2
i=6: '1' → count_ones=3
End: Add 3×4/2=6, result=3+6=9 ✅

Segments found:
- "11" at positions [1,2]: 3 substrings
- "111" at positions [4,5,6]: 6 substrings
Total: 9
```

### Why This Works

Each segment of consecutive 1's can be counted independently. The formula efficiently calculates all possible substrings within that segment without needing nested loops.

**Time Complexity:** O(n) - Single pass through the string
**Space Complexity:** O(1) - Only using constant extra space

## Solution

Implementation: [solution.py](./solution.py)

## Complexity Analysis

- **Time Complexity:** O(n)
  - Single pass through the string
  - Constant time operations per character
  
- **Space Complexity:** O(1)
  - Only using a few variables (result, count_ones)
  - No additional data structures needed 
