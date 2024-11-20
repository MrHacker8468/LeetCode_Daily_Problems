
# LeetCode Problem 2516. Take K of Each Character From Left and Right

### Problem Description

Given a string `s` consisting of characters 'a', 'b', and 'c', and a non-negative integer `k`, find the minimum number of minutes to take at least `k` of each character.

### Problem Link
- **LeetCode Problem**: "https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/description/?envType=daily-question&envId=2024-11-20"
- **Difficulty**: Medium

### Example Test Cases

1. **Input**: s = "aabaaaacaabc", k = 2
   - **Output**: 8
   - **Explanation**: Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.

2. **Input**: s = "a", k = 1
   - **Output**: -1
   - **Explanation**: It is not possible to take one 'b' or 'c' so return -1.
   ### Solution Approach

The solution uses a sliding window technique to efficiently solve the problem:
- Count total character occurrences
- Use a dynamic window to minimize time taken
- Track minimum window satisfying the character count requirement

### Code Solution

```python
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Count total characters
        count = [0, 0, 0]
        for c in s:
            count[ord(c) - ord('a')] += 1

        # Check if possible to collect k of each
        if min(count) < k:
            return -1

        res = float('inf')
        l = 0
        
        # Sliding window
        for r in range(len(s)):
            count[ord(s[r]) - ord('a')] -= 1

            # Adjust left boundary
            while min(count) < k:
                count[ord(s[l]) - ord('a')] += 1
                l += 1

            # Update minimum minutes
            res = min(res, len(s) - (r - l + 1))

        return res
```

### Complexity Analysis
- **Time Complexity**: O(n), where n is string length
- **Space Complexity**: O(1)

### Key Concepts
- Sliding Window
- Character Counting
- Minimum Time Calculation

### Tags
- Array Manipulation
- Sliding Window
- String Processing

## How to Use

1. Copy the solution class into your LeetCode submission
2. Test with provided examples
3. Modify and optimize as needed

## Notes
- Solution handles edge cases
- Efficiently tracks character requirements
- Minimizes time complexity

## Contributions
Open to optimizations and alternative approaches!


The README provides a comprehensive overview of the problem, solution, and context. It follows a typical LeetCode solution repository structure. Would you like me to modify anything?