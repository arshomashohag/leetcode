# 717. 1-bit and 2-bit Characters

**Difficulty:** Easy  
**Date:** November 18, 2025 (Daily Challenge)  
**Topics:** Array  
**Acceptance Rate:** 45.6%

## Problem Description

We have two special characters:
- The first character can be represented by one bit `0`.
- The second character can be represented by two bits (`10` or `11`).

Given a binary array `bits` that ends with `0`, return `true` if the last character must be a one-bit character.

### Example 1:
```
Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
```

### Example 2:
```
Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.
```

### Constraints:
- `1 <= bits.length <= 1000`
- `bits[i]` is either `0` or `1`.

### Hint:
Keep track of where the next character starts. At the end, you want to know if you started on the last bit.

---

## Approach & Algorithm

### Recursive Traversal with Character Decoding

The solution uses a recursive approach to traverse the bit array, decoding characters according to the rules and checking if we land exactly on the last bit.

**Key Insight:** If we can decode the array by following the character rules and land exactly on the last index, then the last character must be a 1-bit character (`0`).

**Character Decoding Rules:**
- If we see a `1`, it starts a 2-bit character (`10` or `11`), so we skip 2 positions
- If we see a `0`, it's a 1-bit character, so we skip 1 position

**Algorithm:**
1. Handle edge cases:
   - If last bit is `1`: impossible (array guaranteed to end with `0`)
   - If array length is 1: must be `[0]` → return True
   - If last two bits are `[0,0]`: last character is definitely a 1-bit `0` → return True
2. Use recursive traversal starting from index 0:
   - If we reach exactly `n-1` and it's a `0`: return True (landed on last 1-bit character)
   - If current bit is `1`: jump 2 positions (2-bit character)
   - If current bit is `0`: jump 1 position (1-bit character)
   - If we go out of bounds: return False (couldn't land on last bit)

**Example Walkthrough (`[1,1,1,1,0]`):**
- traverse(0): bits[0]=1 → jump to index 2
- traverse(2): bits[2]=1 → jump to index 4
- traverse(4): index=4, n-1=4, bits[4]=0 → return True ✓

**Example Walkthrough (`[1,1,1,0]`):**
- traverse(0): bits[0]=1 → jump to index 2
- traverse(2): bits[2]=1 → jump to index 4 (out of bounds) → return False ✓

## Solution

Implementation: [solution.py](./solution.py)

## Complexity Analysis

- **Time Complexity:** O(n) - We visit each element at most once during traversal
- **Space Complexity:** O(n) - Recursive call stack can go up to n/2 depth in worst case 
