from typing import List


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """Given a matrix, return the transpose of the matrix

    Args:
        matrix (List[List[int]]): Array of lists

    Returns:
        List[List[int]]: Transpose matrix
    """
    transpose_matrix = []

    # Pop first idx and create arrays in the
    # final array based off its length
    first_arr = matrix.pop(0)
    for arr in first_arr:
        transpose_matrix.append([arr])

    # Keeping popping the list until its empty
    # and use the idx value to determine which
    # array it should be in
    while True:
        if matrix == []:
            break
        arr = matrix.pop(0)
        for idx, a in enumerate(arr):
            transpose_matrix[idx].append(a)

    return transpose_matrix
