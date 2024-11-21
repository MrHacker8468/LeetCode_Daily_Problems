# LeetCode Problem 2257. Count Inguarded Cells in a Grid

### Problem Description

You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.

### Problem Link
- **LeetCode Problem**: "https://leetcode.com/problems/count-unguarded-cells-in-the-grid/description/?envType=daily-question&envId=2024-11-21"
- **Difficulty**: Medium

### Example Test Cases

1. **Input**: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
   - **Output**: 7
   - **Explanation**: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.

2. **Input**:  m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
   - **Output**: 4
   - **Explanation**: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.

# Solution

To solve this problem, we need to determine how the guards' visibility impacts the cells on the grid while avoiding the walls

# Approach
We can break the solution into several steps:

1. Initialize the grid:
Create a 2D grid where each cell can be:
- Empty (0)
- Guard (1)
- Wall (2)
- Guarded (3)
2. Mark the positions of guards and walls:
Place guards and walls in the grid by updating the respective positions.

3. Simulate the guards' visibility:
For each guard, traverse in all four cardinal directions (up, down, left, right), marking cells as guarded until encountering another guard, a wall, or the boundary of the grid.

4. Count unguarded cells:
Finally, count the cells that are still unoccupied and not marked as guarded.

# Complexity
- Time complexity:
$$O(m.n)$$

- Space complexity:
$$O(m.n)$$

# Code
```python []
class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        # initialize ahe grid 
        grid = [[0] * n for _ in range(m)]

        # mark gaurd and walls on the grid

        for r, c in guards:
            grid[r][c] = 1 # Gaurd
        
        for r,c in walls:
            grid[r][c] = 2 # Wall

        # Helper fun to mark cells as guarded
        def mark_guarded(r, c, dr, dc):
            while 0 <= r < m and 0 <= c < n:
                if grid[r][c] == 1 or grid[r][c] == 2:  # Stop at guard or wall
                    break
                if grid[r][c] == 0:  # Mark as guarded if empty
                    grid[r][c] = 3
                r += dr
                c += dc

        # Simulate guards visibility
        for r, c in guards:
            mark_guarded(r - 1, c, -1, 0)  # Up
            mark_guarded(r + 1, c, 1, 0)   # Down
            mark_guarded(r, c - 1, 0, -1)  # Left
            mark_guarded(r, c + 1, 0, 1)   # Right

        # Count the no. of unguarded cells
        unguarded_count = sum(1 for r in range(m) for c in range(n) if grid[r][c] == 0)
        
        return unguarded_count
```

## Explanation of Code

1. ### Grid Initialization
The grid is initialized with `0` (empty cells), and we then update the grid with the positions of:
- **Guards** (`1`)
- **Walls** (`2`)

---

2. ### Mark Guarded Cells
The `mark_guarded` function traverses in the specified direction (`dr`, `dc`) and marks cells as `3` until it encounters:
- Another guard
- A wall

---

3. ### Visibility Simulation
For every guard, we call `mark_guarded` in all four directions:
- **Up**
- **Down**
- **Left**
- **Right**

---

4. ### Count Unguarded Cells
We count all cells that remain as `0` (unoccupied and not guarded).
