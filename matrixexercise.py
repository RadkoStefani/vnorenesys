import numpy as np

def matrix_addition(A,B):
    return np.add(A,B)

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print(matrix_addition(A,B))

def matrix_multi(A,B):
    return A@B

def matrix_transpo(A,B):
    return A.T

def matrix_det(A,B):
    return np.linalg.det(A)

def matrix_inverse(A,B):
    return np.linalg.inv(A)