# 2654. Minimum Number of Operations to Make All Array Elements Equal to 1

**Difficulty:** Medium  
**Date:** November 12, 2025 (Daily Challenge)  
**Topics:** Array, Math, Number Theory  
**Acceptance Rate:** 36.9%

## Problem Description

You are given a **0-indexed** array `nums` consisting of **positive** integers. You can do the following operation on the array **any** number of times:

- Select an index `i` such that `0 <= i < n - 1` and replace either of `nums[i]` or `nums[i+1]` with their gcd value.

Return *the **minimum** number of operations to make all elements of* `nums` *equal to* `1`. If it is impossible, return `-1`.

The gcd of two integers is the greatest common divisor of the two integers.

### Example 1:
```
Input: nums = [2,6,3,4]
Output: 4
Explanation: We can do the following operations:
- Choose index i = 2 and replace nums[2] with gcd(3,4) = 1. Now we have nums = [2,6,1,4].
- Choose index i = 1 and replace nums[1] with gcd(6,1) = 1. Now we have nums = [2,1,1,4].
- Choose index i = 0 and replace nums[0] with gcd(2,1) = 1. Now we have nums = [1,1,1,4].
- Choose index i = 2 and replace nums[3] with gcd(1,4) = 1. Now we have nums = [1,1,1,1].
```

### Example 2:
```
Input: nums = [2,10,6,14]
Output: -1
Explanation: It can be shown that it is impossible to make all the elements equal to 1.
```

### Constraints:
- `2 <= nums.length <= 50`
- `1 <= nums[i] <= 10^6`

### Hints:
1. Note that if you have at least one occurrence of 1 in the array, then you can make all the other elements equal to 1 with one operation each.
2. Try finding the shortest subarray with a gcd equal to 1.

---

## Approach & Algorithm

### Key Insights

1. **If array already contains 1(s):**
   - We can use `gcd(1, x) = 1` to convert any element to 1
   - Total operations = number of non-1 elements = `n - count_of_ones`

2. **If GCD of entire array > 1:**
   - Impossible to create a 1 (no common divisor can be 1)
   - Return `-1`

3. **Otherwise, we need to CREATE a 1 first, then SPREAD it:**
   - Find the shortest contiguous subarray with GCD = 1
   - Convert that subarray into a single 1 (takes `k-1` operations for length `k`)
   - Then spread the 1 to all positions (takes `n-1` operations)
   - **Total operations = `(k - 1) + (n - 1) = k + n - 2`**

### Algorithm Steps

```
1. Count existing 1s in the array
   - If all are 1s → return 0
   - If at least one 1 exists → return (n - count_of_ones)

2. Find shortest subarray with GCD = 1:
   - Use nested loops to check all subarrays
   - For each starting position i:
     - Calculate running GCD from i to j
     - If GCD becomes 1, record the length and break
   - Early termination: GCD can only decrease or stay same

3. Calculate total operations:
   - If no such subarray found → return -1
   - Otherwise → return (shortest_length + n - 2)
```

### Why Shortest Subarray?

A subarray of length `k` with GCD = 1 requires `(k-1)` operations to "collapse" into a single 1:
- Each operation replaces an element with GCD of adjacent pair
- After `k-1` operations, we have at least one 1 in the array
- Shorter subarrays = fewer operations to create the first 1

## Solution

Implementation: [solution.py](./solution.py)

## Complexity Analysis

- **Time Complexity:** O(n² × log(min_value))
  - O(n²) for checking all subarrays
  - O(log(min_value)) for each GCD calculation
  - Early termination makes it faster in practice
  
- **Space Complexity:** O(1)
  - Only using constant extra space for variables
