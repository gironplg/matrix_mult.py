# Author: Gabriel Giron plata
# GitHub username: gironplg
# Date: 5/27/2026
# Description: This code will take two 2D matrices which will be
# represented as a list of lists of numbers and returns their matrix product
def dot_prod(list1,list2):
    total = 0
    for i in range(len(list1)):
        total += list1[i] * list2[i]
    return total

def matrix_mult(A,B):
    if len(A[0]) != len(B):
        return None
    result = []

    for row in A:
        new_row = []
        for col in range(len(B[0])):
            column=[]
            for row_b in B:
                column.append(row_b[col])
            new_row.append(dot_prod(row,column))
        result.append(new_row)
    return result
rows_A = int(input("Enter the number of rows for matrix A: "))
cols_A = int(input("Enter the number of columns for matrix A: "))
A=[]
print("Enter numbers of matrix A:")
for i in range(rows_A):
    row= list(map(int,input(f"row{i+1}:").split()))
    A.append(row)
rows_B = int(input("Enter the number of rows for matrix B: "))
cols_B = int(input("Enter the number of columns for matrix B: "))
B=[]
print("Enter numbers of matrix B:")
for i in range(rows_B):
    row= list(map(int,input(f"row{i+1}:").split()))
    B.append(row)
result = matrix_mult(A,B)
if result is None:
    print("The matcices could not be multiplied")
else:
    print("The result of matrix multiplication is:")
    for row in result:
        print(row)