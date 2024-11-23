# LeetCode Problem 1072. Flip Columns For Maximum Number of Equal Rows

### Problem Description

You are given an m x n binary matrix matrix.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number of flips.

### Problem Link
- **LeetCode Problem**: "https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/description/?envType=daily-question&envId=2024-11-23"
- **Difficulty**: Medium

### Example Test Cases

1. **Input**: matrix = [[0,1],[1,1]]
   - **Output**: 1
   - **Explanation**: After flipping no values, 1 row has all values equal.

2. **Input**:   matrix = [[0,1],[1,0]]
   - **Output**: 2
   - **Explanation**: After flipping values in the first column, both rows have equal values.

# Solution

To solve this problem, we need to determine how the guards' visibility impacts the cells on the grid while avoiding the walls


# Code
```python []
class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        from collections import Counter

        # To store normalized row pattern
        pattern_counts = Counter()

        for row in matrix:
            normailized = tuple(row[i] ^ row[0] for i in range(len(row)))
            pattern_counts[normailized] += 1

        return max(pattern_counts.values())
```