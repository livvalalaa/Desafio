import numpy as np

A = np.array([[3, 1], [2, 4]])
det_A = np.linalg.det(A)
print("Determinante de A (2x2):", det_A)

B = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
det_B = np.linalg.det(B)
print("Determinante de B (3x3):", det_B)
