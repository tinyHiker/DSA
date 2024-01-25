# 2D List
def diagonal_sum(matrix):
    # Initialize the sum to 0
    total = 0

    # Iterate through the rows of the matrix
    for i in range(len(matrix)):
        # Add the diagonal element to the total sum
        total += matrix[i][i]

    return total
