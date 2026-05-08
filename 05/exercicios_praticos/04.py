import numpy as np

A = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
det = np.linalg.det(A)
print("Determinante:", det)

det = np.linalg.det(A)

if det != 0:
    print("O sistema é possível.")
else:
    print("O sistema não é resolvível, não em uma única solução.")
