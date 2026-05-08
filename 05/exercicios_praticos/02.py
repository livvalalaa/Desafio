A = [[10, 50, 35]]
B = [[20, 70, 30]]

C_adicao = [[0, 0, 0]]
for i in range(1):
    for j in range(3):
        C_adicao[i][j] = A[i][j] + B[i][j]

print("Matriz soma:", C_adicao)

total = 0
for linha in C_adicao:
    for valor in linha:
        total += valor

print("Total das vendas:", total)
