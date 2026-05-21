# Author: Gabriel Giron plata
# GitHub username: gironplg
# Date: 5/27/2026
# Description: This code takes 2 different list of numbers and takes the dot product of the 2
def dot_product(a,b):
    """
    Calculate the dot product of two vectors
    Args:
    A:The first vector
    B:The second vector
    Returns:
    The dot product of the two vectors
    """
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result
input_a = input("Enter the numbers of the first vector separated by space: ")
vector_a = [int(x) for x in input_a.split()]

input_b = input("Enter the numbers of the second vector separated by space: ")
vector_b = [int(x) for x in input_b.split()]

if len(vector_a) != len(vector_b):
    print("The vectors do not have the same length")
else:
    dot_product_result = dot_product(vector_a, vector_b)
    print(f"The dot product of the two vectors is {dot_product_result}")
