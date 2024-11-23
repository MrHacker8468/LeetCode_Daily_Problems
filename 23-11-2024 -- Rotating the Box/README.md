# LeetCode Problem 1861: Rotating the Box 🎲

## Problem Description 🎯
Given an `m x n` matrix representing a side-view of a box, rotate it 90 degrees clockwise and simulate gravity affecting the stones. The box contains:
- Stones (`'#'`)
- Stationary obstacles (`'*'`)
- Empty spaces (`'.'`)

After rotation, stones fall due to gravity until they hit:
- An obstacle
- Another stone
- The bottom of the box

### Key Rules
- Obstacles remain fixed in position
- Rotation doesn't affect stones' horizontal positions
- All stones will rest on a solid surface
- Gravity only affects vertical movement

## Examples

### Example 1
```
Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]
```

### Example 2
```
Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
```

### Example 3
```
Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
```

## Solution Approach 💡

### Algorithm Overview
1. **Process Gravity in Original Box**
   - Scan each row from right to left
   - Track the rightmost empty position
   - Move stones to empty positions when possible
   - Reset empty position tracker at obstacles

2. **Rotate the Box**
   - Create new matrix with swapped dimensions
   - Copy elements with rotation transformation
   - Apply formula: `rotated[j][m-1-i] = original[i][j]`

### Implementation
```python
def rotateTheBox(self, box):
    m, n = len(box), len(box[0])
    
    # Process gravity in original orientation
    for row in box:
        empty = n - 1  # Rightmost empty position
        for col in range(n - 1, -1, -1):
            if row[col] == '*':
                empty = col - 1
            elif row[col] == '#':
                if empty != col:
                    row[col], row[empty] = '.', '#'
                    empty -= 1
                else:
                    empty -= 1
    
    # Rotate the box
    rotated_box = [[None] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            rotated_box[j][m - 1 - i] = box[i][j]
    
    return rotated_box
```

## Complexity Analysis ⚙️

### Time Complexity
- **O(m·n)** where m and n are box dimensions
- We process each cell twice:
  1. Once for gravity simulation
  2. Once for rotation

### Space Complexity
- **O(m·n)** for the rotated box matrix
- Original matrix is modified in-place during gravity simulation

## Constraints ⚓
- `m == box.length`
- `n == box[i].length`
- `1 <= m, n <= 500`
- `box[i][j]` is one of `'#'`, `'*'`, or `'.'`

## Key Insights 🔑
1. Process gravity before rotation to simplify logic
2. Use two-pointer technique for efficient stone movement
3. Matrix rotation follows fixed pattern
4. In-place modification reduces space complexity

## Common Pitfalls 🚧
1. Forgetting to process gravity before rotation
2. Incorrect rotation transformation
3. Not handling obstacles properly
4. Wrong empty position tracking



## Contributing 🤝
Feel free to submit issues and enhancement requests!

