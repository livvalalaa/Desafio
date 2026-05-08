import numpy as np

A = np.array([[3, 1], [2, 4]])
if np.linalg.det(A) != 0:
    inversa = np.linalg.inv(A)
    print("Inversa de A:\n", inversa)
else:
    print("Matriz não ivertível.")
