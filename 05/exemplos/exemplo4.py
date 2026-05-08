import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
E = np.array([[7, 8], [9, 10], [11, 12]])

F_multi = np.dot(A, E)
print("Multiplcação de matrizes:\n", F_multi)
