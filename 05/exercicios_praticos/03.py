import numpy as np

dados = np.array([[6.0, 5.5, 9.0], [8.3, 7.4, 10.0], [7.0, 9.0, 9.5]])

medias = []

for i in range(len(dados)):
    soma = 0

    for j in range(len(dados[i])):
        soma += dados[i][j]

    media = soma / len(dados[i])
    medias.append(media)

print("Médias dos alunos:", medias)
