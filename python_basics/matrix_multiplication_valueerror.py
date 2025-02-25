
def dot_product(row,col):
    dot_sum = 0
    for r in range(len(row)):
        dot_sum += row[r]*col[r]
    return(dot_sum)

def matrix_multiplication_2d(A, B):

    # in matrix multiplication, we define the product
    # AB as the dot product of
    # each row of A with each column of B

    if len(A[0]) != len(B):
        raise ValueError('The row length of A must equal the column length of B')

    # get the rows of A
    row_A1 = A[0]
    row_A2 = A[1]

    # get the cols of B
    col_B1 = []
    col_B2 = []
    for i in range(len(B)):
        col_B1.append(B[i][0])
        col_B2.append(B[i][1])

    # define the result matrix
    AB = [[], []]
    AB[0].append(dot_product(row_A1, col_B1))
    AB[0].append(dot_product(row_A1, col_B2))
    AB[1].append(dot_product(row_A2, col_B1))
    AB[1].append(dot_product(row_A2, col_B2))

    return(AB)
