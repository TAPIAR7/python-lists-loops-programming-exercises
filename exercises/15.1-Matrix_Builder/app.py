#Import random

#Create the function below:
def matrixBuilder(number):
    matrix =[]
    # Create first the matrix
    for i in range(number):
        matrix.append(list(range(number)))
    # update values
    for row in range(number):
        for col in range(number):
            matrix[row][col] = 1
    return matrix

print(matrixBuilder(9))
