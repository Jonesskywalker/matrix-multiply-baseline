import numpy as np

# Simple matrix multiplication example
A = np.random.rand(100, 100)
B = np.random.rand(100, 100)
C = np.dot(A, B)

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Result C:\n", C)