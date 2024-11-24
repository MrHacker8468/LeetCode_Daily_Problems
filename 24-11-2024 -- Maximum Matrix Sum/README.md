# LeetCode Problem 1975: Maximum Matrix Sum 🔢

## Problem Description 🎯
Given an `n x n` integer matrix, perform the following operation any number of times:
- Choose any two **adjacent** elements
- Multiply both elements by `-1`

The goal is to maximize the sum of all matrix elements. Adjacent elements share a border (up, down, left, or right).

### Key Concepts
- Elements can be negated multiple times
- Only adjacent pairs can be modified
- Diagonal elements are not considered adjacent
- Operations can be performed in any order

## Examples

### Example 1
```
Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation:
1. Multiply first row by -1: [[-1,1],[-1,1]]
2. Multiply first column by -1: [[1,1],[1,1]]
Final sum = 1 + 1 + 1 + 1 = 4
```

### Example 2
```
Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation:
1. Multiply last two elements in second row by -1
2. Final matrix has all positive values except -1
Sum = 1 + 2 + 3 + 1 + 2 + 3 + 1 + 2 + 3 = 16
```

## Solution Approach 💡

### Key Insights
1. The order of operations doesn't matter
2. Pairs of negative numbers can always be made positive
3. Only the parity of negative numbers matters
4. If odd negatives exist, one number must remain negative

### Algorithm
```python
def maxMatrixSum(self, matrix):
    n = len(matrix)
    total_sum = 0
    negative_count = 0
    min_abs_value = float('inf')
    
    # Step 1: Process matrix
    for i in range(n):
        for j in range(n):
            val = matrix[i][j]
            total_sum += abs(val)  # Sum absolute values
            if val < 0:
                negative_count += 1  # Count negatives
            min_abs_value = min(min_abs_value, abs(val))  # Track minimum
    
    # Step 2: Adjust for odd negatives
    if negative_count % 2 == 1:
        total_sum -= 2 * min_abs_value
    
    return total_sum
```

### Implementation Details
1. **Matrix Processing**
   - Calculate sum of absolute values
   - Count negative numbers
   - Track minimum absolute value

2. **Final Calculation**
   - If even negatives: return absolute sum
   - If odd negatives: subtract twice the minimum absolute value

## Complexity Analysis ⚙️

### Time Complexity
- **O(n²)** where n is the matrix dimension
- Single pass through matrix

### Space Complexity
- **O(1)** constant extra space
- Only tracking counts and sums


## Constraints ⚓
- `n == matrix.length == matrix[i].length`
- `2 <= n <= 250`
- `-10⁵ <= matrix[i][j] <= 10⁵`

## Edge Cases 🔍
1. All positive numbers
2. All negative numbers
3. Single negative number
4. Matrix with zeros
5. Maximum/minimum value boundaries


## Contributing 🤝
Feel free to submit issues and enhancement requests!
