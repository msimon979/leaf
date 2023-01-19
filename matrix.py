# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]


def transpose(matrix):
    transpose_matrix = []

    first_arr = matrix.pop(0)
    len_first_arr = len(first_arr)

    for arr in first_arr:
        transpose_matrix.append([arr])

    # print(transpose_matrix, matrix)

    for m in matrix:
        counter = len_first_arr - 1
        while counter != 0:
            print(transpose_matrix, m)
            transpose_matrix[counter].append(m.pop())
            counter -= 1
            break

    # while True:
    #     if matrix == []:
    #         break

    #     arr = matrix.pop(0)
    #     for idx, a in enumerate(arr):
    #         transpose_matrix[idx].append(a)

    print(transpose_matrix)


transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
