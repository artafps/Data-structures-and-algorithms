from tabulate import tabulate

n = int(input("The number of rows of the matrix :"))
m = int(input("The number of columns of the matrix :"))
while n<2 and m<2 :
    n = int(input("The number of rows and columns of the matrix :"))
matrix = []
matrixSparse = [[n,m,0]]
for i in range(0,n,1):
    rows = []
    for j in range(0,m,1):
        print("The row",i ,"of the column",j,":+>")
        inp=int(input())
        if(inp!=0):
            matrixSparse[0][2] += 1
            matrixSparse.append([i,j,inp])
        rows.append(inp)
    matrix.append(rows)

print("Normal matrix")

print(tabulate(matrix,  tablefmt="grid"))

print("Storing the matrix using the sparse method")

print("loading ........")
print("Sparse matrix")
print(tabulate(matrixSparse,tablefmt="grid"))
