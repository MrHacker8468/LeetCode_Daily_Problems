
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

## Solution Explanation

### Frequency Check
First, the function checks the frequency of each character ('a', 'b', and 'c') in the string `s`. If the minimum count of any character is less than `k`, it means it is impossible to collect at least `k` of each character. In such cases, the function immediately returns `-1`.

### Sliding Window
The solution uses a **sliding window approach** with two pointers: `l` (left pointer) and `r` (right pointer). Initially, the `l` pointer starts from the beginning of the string, while the `r` pointer iterates through the string from left to right.

At each step, the function tracks the number of characters collected using the `count` array, which stores the count of characters 'a', 'b', and 'c'.

### Right Pointer Movement
As the `r` pointer moves through the string:
- The corresponding character count in the `count` array is decremented (since we are collecting the character).
- The function checks if the minimum count of any character in `count` is still below `k`. If it is, the function continues adjusting the window.

### Left Pointer Adjustment
Whenever the minimum character count in `count` falls below `k`, the `l` pointer is moved forward. This process is repeated until the window size has enough characters such that all the counts of 'a', 'b', and 'c' meet or exceed `k`. The corresponding character count in `count` is incremented as the `l` pointer moves.

### Minimum Time Calculation
At each step, the function calculates the current window size (the number of characters between `l` and `r`). It then updates the result (`res`) if the current window size is smaller than the previous minimum window.

### Return Minimum Time
After the iteration finishes, the function returns the smallest window size (`res`) that satisfies the condition of collecting at least `k` characters of 'a', 'b', and 'c'. This value represents the **minimum number of minutes** required.


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