import random

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        matriz[i][j] = random.randint(1, 100)

for linha in matriz:
    print(linha)
