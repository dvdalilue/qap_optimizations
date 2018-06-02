# np functions

def swapRows(matrix, i_1, i_2):
    row_1 = matrix[i_1].copy()
    matrix[i_1] = matrix[i_2]
    matrix[i_2] = row_1

def swapColumns(matrix, j_1, j_2):
    matrix = matrix.transpose()
    swapRows(matrix, j_1, j_2)
    matrix = matrix.transpose()

def equivalenceRatio(a_1, a_2):
    n = len(a_1) # == len(a_2)
    equivalence = 0.0
    for i in xrange(0, n):
        if a_1[i] == a_2[i]:
            equivalence += 1.0

    return (equivalence / float(n))