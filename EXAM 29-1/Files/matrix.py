""" func3: 6 marks

Define the function 
    func3(input_filename, output_filename)
which receives the following arguments:
- input_filename: the path to a text file containing a rectangular matrix 
    of integers with N rows and 2N columns
- output_filename: the path to a file in which you must write a square matrix
    NxN 
The function must read the N x 2N matrix of integers and transform it 
into an NxN square matrix in which the value in cell i,j is obtained by adding:
- the value of the cell in row i and column N+j
- all the elements in column j.
The function must also return the sum of all the elements in the input matrix.

Example: the file func3/in_5.txt contains the matrix
    1 2 1 2
    2 3 2 3
the function must transform it into the matrix
    4 7
    5 8

[i][j] = matrix[i][h + j]
write the matrix in the output file and return 16.

"""






def func3(input_filename, output_filename):

    matrix=matrix_finder(input_filename)
    N = len(matrix)

    with open(output_filename,'w') as fout:
        for i in range(N):
            row =[]
            for j in range(N):
                value = matrix[i][N + j] + sum(matrix[k][j] for k in range(N))
                row.append(value)
            fout.write(' '.join(str(x) for x in row)+'\n' )
    
    total=0
    for lis in matrix:
        for k in lis:
            total += k

    return total


def matrix_finder(input_filename):
    matri = []
    with open(input_filename,'r') as f:
        for line in f:
            matri.append(list(map(int,line.split())))
    return matri


