
matrixA = [[1, 2, 3], [4, 5, 6]]

matrixB = [[7, 8], [9, 10], [11, 12]]


def sparse_matrix_multiplication(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]

    sparse_a = get_dict_nonzero(matrix_a)
    sparse_b = get_dict_nonzero(matrix_b)

    # make empty column with # rows =  # rows in matrix_a and columns
    # = # columns in matrix b
    matrix_c = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]

    for i, k in sparse_a.keys():
        for j in range(len(matrix_b[0])):
            if (k, j) in sparse_b.keys():
                matrix_c[i][j] += sparse_a[(i, k)] * sparse_b[(k, j)]
    return matrix_c


def get_dict_nonzero(matrix):
    dict_nonzeros = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                dict_nonzeros[(i, j)] = matrix[i][j]
    return dict_nonzeros
