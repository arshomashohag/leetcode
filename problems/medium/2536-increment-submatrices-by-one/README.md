# 2536. Increment Submatrices by One

**Difficulty:** Medium  
**Date:** November 14, 2025 (Daily Challenge)  
**Topics:** Array, Matrix, Prefix Sum  
**Acceptance Rate:** 69.2%

## Problem Description

You are given a positive integer `n`, indicating that we initially have an `n x n` **0-indexed** integer matrix `mat` filled with zeroes.

You are also given a 2D integer array `query`. For each `query[i] = [row1ᵢ, col1ᵢ, row2ᵢ, col2ᵢ]`, you should do the following operation:

- Add `1` to **every element** in the submatrix with the **top left** corner `(row1ᵢ, col1ᵢ)` and the **bottom right** corner `(row2ᵢ, col2ᵢ)`. That is, add `1` to `mat[x][y]` for all `row1ᵢ <= x <= row2ᵢ` and `col1ᵢ <= y <= col2ᵢ`.

Return *the matrix* `mat` *after performing every query.*

### Example 1:
```
Input: n = 3, queries = [[1,1,2,2],[0,0,1,1]]
Output: [[1,1,0],[1,2,1],[0,1,1]]
Explanation: The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
- In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
- In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).
```

### Example 2:
```
Input: n = 2, queries = [[0,0,1,1]]
Output: [[1,1],[1,1]]
Explanation: The diagram above shows the initial matrix and the matrix after the first query.
- In the first query we add 1 to every element in the matrix.
```

### Constraints:
- `1 <= n <= 500`
- `1 <= queries.length <= 10⁴`
- `0 <= row1ᵢ <= row2ᵢ < n`
- `0 <= col1ᵢ <= col2ᵢ < n`

### Hints:
1. Imagine each row as a separate array. Instead of updating the whole submatrix together, we can use prefix sum to update each row separately.
2. For each query, iterate over the rows i in the range [row1, row2] and add 1 to prefix sum S[i][col1], and subtract 1 from S[i][col2 + 1].
3. After doing this operation for all the queries, update each row separately with S[i][j] = S[i][j] + S[i][j - 1].

---

## Approach & Algorithm

### Key Insight

Instead of updating each cell in the submatrix (which would be O(n²) per query), we use a **2D Difference Array** technique. This allows us to mark range boundaries in O(1) and then compute the final result with a single pass.

### 2D Difference Array Technique

The core idea is to mark only the **corners** of each rectangular region:

1. **Mark the top-left corner** `(r1, c1)` with `+1` (start of the region)
2. **Mark beyond the top-right** `(r1, c2+1)` with `-1` (stop incrementing columns)
3. **Mark beyond the bottom-left** `(r2+1, c1)` with `-1` (stop incrementing rows)
4. **Mark the bottom-right diagonal** `(r2+1, c2+1)` with `+1` (cancel the double subtraction)

After marking all boundaries, apply **2D prefix sum** to compute the actual values.

### Algorithm Steps

```
1. Initialize n×n matrix with zeros

2. For each query [r1, c1, r2, c2]:
   - mat[r1][c1] += 1
   - mat[r1][c2+1] -= 1 (if within bounds)
   - mat[r2+1][c1] -= 1 (if within bounds)
   - mat[r2+1][c2+1] += 1 (if within bounds)

3. Apply prefix sum across rows:
   for each row r:
       for c from 1 to n-1:
           mat[r][c] += mat[r][c-1]

4. Apply prefix sum down columns:
   for each column c:
       for r from 1 to n-1:
           mat[r][c] += mat[r-1][c]

5. Return mat
```

### Visual Example

```
Query: Add 1 to submatrix (1,1) to (2,2) in 4×4 matrix

Step 1: Mark boundaries
    0  1  2  3
  ┌──┬──┬──┬──┐
0 │ 0│ 0│ 0│ 0│
  ├──┼──┼──┼──┤
1 │ 0│+1│ 0│-1│  ← Mark (1,1) and (1,3)
  ├──┼──┼──┼──┤
2 │ 0│ 0│ 0│ 0│
  ├──┼──┼──┼──┤
3 │ 0│-1│ 0│+1│  ← Mark (3,1) and (3,3)
  └──┴──┴──┴──┘

Step 2: Apply horizontal prefix sum
    0  1  2  3
  ┌──┬──┬──┬──┐
0 │ 0│ 0│ 0│ 0│
  ├──┼──┼──┼──┤
1 │ 0│ 1│ 1│ 0│
  ├──┼──┼──┼──┤
2 │ 0│ 0│ 0│ 0│
  ├──┼──┼──┼──┤
3 │ 0│-1│-1│ 0│
  └──┴──┴──┴──┘

Step 3: Apply vertical prefix sum
    0  1  2  3
  ┌──┬──┬──┬──┐
0 │ 0│ 0│ 0│ 0│
  ├──┼──┼──┼──┤
1 │ 0│ 1│ 1│ 0│
  ├──┼──┼──┼──┤
2 │ 0│ 1│ 1│ 0│  ✅ Final result
  ├──┼──┼──┼──┤
3 │ 0│ 0│ 0│ 0│
  └──┴──┴──┴──┘
```

### Why It Works

- Horizontal prefix sum spreads the increment across columns within marked rows
- Vertical prefix sum spreads the increment down to all rows in the range
- The boundary markers ensure the increment only affects the desired rectangle
- The `+1` at bottom-right cancels the double subtraction from the two `-1` marks

## Solution

Implementation: [solution.py](./solution.py)

## Complexity Analysis

- **Time Complexity:** O(Q + n²)
  - O(Q) to process all queries and mark boundaries
  - O(n²) for the two prefix sum passes (horizontal and vertical)
  - Much better than naive O(Q × n²) approach
  
- **Space Complexity:** O(n²)
  - Output matrix of size n×n
  - No additional space needed beyond the result 
