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