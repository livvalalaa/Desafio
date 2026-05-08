A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

C_adicao = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        C_adicao[i][j] = A[i][j] + B[i][j]

print("Adição das matrizes:", C_adicao)

D_subtracao = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        D_subtracao[i][j] = A[i][j] - B[i][j]

print("Subtração das matrizes (A - B):", D_subtracao)
