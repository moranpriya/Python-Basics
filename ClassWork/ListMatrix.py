def read_matrix(rows, cols):
    matrix = []
    print("Enter the elements row by row :")
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    print("The matrix is :")
    for row in matrix:
        print(row)

# Main program
r = int(input("Enter number of rows : "))
c = int(input("Enter number of columns : "))

mat = read_matrix(r, c)
display_matrix(mat)