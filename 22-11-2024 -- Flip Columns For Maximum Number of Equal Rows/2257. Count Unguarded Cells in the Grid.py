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