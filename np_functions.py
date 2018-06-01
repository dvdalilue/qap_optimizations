# np functions

def swapRows(matrix, i_1, i_2):
    row_1 = matrix[i_1].copy()
    matrix[i_1] = matrix[i_2]
    matrix[i_2] = row_1

def swapColumns(matrix, j_1, j_2):
    matrix = matrix.transpose()
    swapRows(matrix, j_1, j_2)
    matrix = matrix.transpose()