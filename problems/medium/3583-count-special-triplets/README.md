# 3583. Count Special Triplets

**Difficulty:** Medium  
**Date:** December 9, 2025 (Daily Challenge)  
**Topics:** Array, Hash Table, Counting  
**Acceptance Rate:** 38.4%

## Problem Description

You are given an integer array `nums`.

A **special triplet** is defined as a triplet of indices `(i, j, k)` such that:
- `0 <= i < j < k < n`, where `n = nums.length`
- `nums[i] == nums[j] * 2`
- `nums[k] == nums[j] * 2`

Return the total number of **special triplets** in the array.

Since the answer may be large, return it **modulo** `10^9 + 7`.

### Example 1:
```
Input: nums = [6,3,6]
Output: 1
Explanation:
The only special triplet is (i, j, k) = (0, 1, 2), where:
- nums[0] = 6, nums[1] = 3, nums[2] = 6
- nums[0] = nums[1] * 2 = 3 * 2 = 6
- nums[2] = nums[1] * 2 = 3 * 2 = 6
```

### Example 2:
```
Input: nums = [0,1,0,0]
Output: 1
Explanation:
The only special triplet is (i, j, k) = (0, 2, 3), where:
- nums[0] = 0, nums[2] = 0, nums[3] = 0
- nums[0] = nums[2] * 2 = 0 * 2 = 0
- nums[3] = nums[2] * 2 = 0 * 2 = 0
```

### Example 3:
```
Input: nums = [8,4,2,8,4]
Output: 2
Explanation:
There are exactly two special triplets:
- (i, j, k) = (0, 1, 3): nums[0] = 8, nums[1] = 4, nums[3] = 8
- (i, j, k) = (1, 2, 4): nums[1] = 4, nums[2] = 2, nums[4] = 4
```

### Constraints:
- `3 <= n == nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`

### Hints:
1. Use frequency arrays or maps, e.g. `freqPrev` and `freqNext`—to track how many times each value appears before and after the current index.
2. For each index `j` in the triplet (`i`,`j`,`k`), compute its contribution to the answer using your freqPrev and freqNext counts.

---

## Approach & Algorithm

### Two-Pass Frequency Counting

The solution uses a two-pass approach with hash maps to efficiently count special triplets without checking all possible combinations.

**Key Insight:** For each middle index `j`, we need to count how many valid `i` positions exist before it (where `nums[i] == nums[j] * 2`) and how many valid `k` positions exist after it (where `nums[k] == nums[j] * 2`). The product of these counts gives us all valid triplets with `j` as the middle element.

**Algorithm:**

1. **First Pass (Left to Right):**
   - Maintain `count_from_left` hash map to track frequency of values seen so far
   - For each position `j`:
     - Calculate `target = nums[j] * 2`
     - Store count of how many times `target` appeared before position `j` in `results[j]`
     - Add `nums[j]` to the frequency map for future positions

2. **Second Pass (Right to Left):**
   - Maintain `count_from_right` hash map to track frequency of values seen so far (from right)
   - For each position `j` (going backwards):
     - Calculate `target = nums[j] * 2`
     - Multiply `results[j]` (count from left) by frequency of `target` on the right
     - Add this product to the total count
     - Add `nums[j]` to the frequency map

3. **Return result modulo 10^9 + 7**

**Example Walkthrough for `[8,4,2,8,4]`:**

First pass (left to right):
- i=0: nums[0]=8, target=16, count_left=0, results[0]=0
- i=1: nums[1]=4, target=8, count_left=1, results[1]=1
- i=2: nums[2]=2, target=4, count_left=1, results[2]=1
- i=3: nums[3]=8, target=16, count_left=0, results[3]=0
- i=4: nums[4]=4, target=8, count_left=2, results[4]=2

Second pass (right to left):
- i=4: nums[4]=4, target=8, results[4]=2, count_right=0, total += 2*0 = 0
- i=3: nums[3]=8, target=16, results[3]=0, count_right=1, total += 0*0 = 0
- i=2: nums[2]=2, target=4, results[2]=1, count_right=1, total += 1*1 = 1
- i=1: nums[1]=4, target=8, results[1]=1, count_right=1, total += 1*1 = 2
- i=0: nums[0]=8, target=16, results[0]=0, count_right=2, total += 0*0 = 2

Result: 2 (triplets are (0,1,3) and (1,2,4))

## Solution

Implementation: [solution.py](./solution.py)

## Complexity Analysis

- **Time Complexity:** O(n) - Two passes through the array with constant time hash map operations
- **Space Complexity:** O(n) - Hash maps store at most n unique values, plus the results array 
