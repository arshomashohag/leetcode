# 1437. Check If All 1's Are at Least Length K Places Away

**Difficulty:** Easy  
**Date:** November 17, 2025 (Daily Challenge)  
**Topics:** Array  
**Acceptance Rate:** 59.3%

## Problem Description

Given an binary array `nums` and an integer `k`, return `true` if all 1's are at least `k` places away from each other, otherwise return `false`.

### Example 1:
```
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.
```

### Example 2:
```
Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.
```

### Constraints:
- `1 <= nums.length <= 10^5`
- `0 <= k <= nums.length`
- `nums[i]` is `0` or `1`

---

## Approach & Algorithm

### Single Pass Tracking

The solution uses a single pass through the array to track the positions of consecutive 1's and verify the distance between them.

**Key Insight:** We only need to track the index of the last 1 encountered and check if the current 1 has at least k elements between them.

**Algorithm:**
1. Initialize `last_one_index` to `-k-1` to handle the edge case where the first 1 appears within the first k positions
2. Iterate through the array with index `i`:
   - When we encounter a 1:
     - Calculate the number of elements between the last 1 and current 1: `i - last_one_index - 1`
     - If this distance is less than k (i.e., `i - last_one_index <= k`), return False
     - Update `last_one_index` to current position `i`
3. If we complete the iteration without finding violations, return True

**Example Walkthrough (nums = [1,0,0,1,0,1], k = 2):**
- i=0: num=1, last_one_index=-3, distance=3 (OK), update last_one_index=0
- i=3: num=1, last_one_index=0, distance=3 (OK), update last_one_index=3
- i=5: num=1, last_one_index=3, distance=2 ≤ 2 (FAIL) → return False

## Solution

Implementation: [solution.py](./solution.py)

## Complexity Analysis

- **Time Complexity:** O(n) - Single pass through the array
- **Space Complexity:** O(1) - Only constant extra space for tracking the last index 
