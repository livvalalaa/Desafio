from exemplo1 import notas

print("Nota do Aluno 1 na discplina 2:", notas[0][1])

notas[1][2] = 9.0
print("Média atualizada:", notas)

media_aluno1 = (notas[0][0] + notas[0][1] + notas[0][2]) / 3
print("Média do aluno 1:", media_aluno1)
