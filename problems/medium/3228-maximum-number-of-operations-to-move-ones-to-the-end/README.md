# 3228. Maximum Number of Operations to Move Ones to the End

**Difficulty:** Medium  
**Date:** November 13, 2025 (Daily Challenge)  
**Topics:** String, Greedy, Counting  
**Acceptance Rate:** 56.2%

## Problem Description

You are given a binary string `s`.

You can perform the following operation on the string **any** number of times:

- Choose **any** index `i` from the string where `i + 1 < s.length` such that `s[i] == '1'` and `s[i + 1] == '0'`.
- Move the character `s[i]` to the **right** until it reaches the end of the string or another `'1'`. For example, for `s = "010010"`, if we choose `i = 1`, the resulting string will be `s = "0**001**10"`.

Return the **maximum** number of operations that you can perform.

### Example 1:
```
Input: s = "1001101"
Output: 4
Explanation:
We can perform the following operations:
- Choose index i = 0. The resulting string is s = "001101".
- Choose index i = 4. The resulting string is s = "001101".
- Choose index i = 3. The resulting string is s = "001011".
- Choose index i = 2. The resulting string is s = "000111".
```

### Example 2:
```
Input: s = "00111"
Output: 0
```

### Constraints:
- `1 <= s.length <= 10^5`
- `s[i]` is either `'0'` or `'1'`

### Hints:
1. It is optimal to perform the operation on the lowest index possible each time.
2. Traverse the string from left to right and perform the operation every time it is possible.

---

## Approach & Algorithm

### Key Insight

Instead of simulating each move operation, we can calculate the total operations by observing a pattern:

**Each '1' that has '0's after it will perform operations equal to the number of times it needs to jump over those '0's.**

Flipping the perspective: **When we see a '1' followed by a '0', that '1' (and all '1's before it) will eventually need to move past that '0'.**

### Algorithm

1. **Maintain a running count** of all '1's seen so far (prefix count)
2. **Traverse left to right** through the string
3. **When we encounter a '1' followed by a '0'** (pattern "10"):
   - All the '1's we've seen so far (including this one) will need to jump over the upcoming '0's
   - Add the current count of '1's to the result
4. This automatically handles groups of consecutive '0's because we only count once when we see the "10" pattern

### Example Walkthrough

```
s = "1001101"

i=0: '1' → count=1, next is '0' → result += 1 = 1
i=1: '0' → count=1
i=2: '0' → count=1  
i=3: '1' → count=2, next is '1' → skip
i=4: '1' → count=3, next is '0' → result += 3 = 4
i=5: '0' → count=3
i=6: '1' → count=4, next is end → skip

Result: 4 ✅
```

### Why It Works

- When a '1' is followed by '0', it means this '1' will eventually move right
- Every '1' before it will also move right past those same '0's
- By counting at the "10" boundary, we capture all operations that will happen
- Groups of consecutive '0's are naturally handled since we only trigger once at the "10" transition

## Solution

Implementation: [solution.py](./solution.py)

## Complexity Analysis

- **Time Complexity:** O(n)
  - Single pass through the string
  - Constant time operations at each position
  
- **Space Complexity:** O(n)
  - Dictionary to store prefix count of '1's at each position
  - Can be optimized to O(1) by using a single counter variable 
