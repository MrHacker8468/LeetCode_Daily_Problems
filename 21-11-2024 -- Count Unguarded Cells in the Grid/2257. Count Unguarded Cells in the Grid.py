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