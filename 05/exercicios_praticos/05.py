import numpy as np

estoque = np.array([[30, 45, 87], [70, 20, 10]])

estoque_T = estoque.T

precos = np.array([[25.0], [30.5]])

totais = np.dot(estoque_T, precos)

print("Estoque transposto:")
print(estoque_T)

print("Totais calculados:")
print(totais)
