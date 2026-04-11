import cadastro
import calculos


def cadastros_funcionario(dados):
    tipo = dados["Tipo"]
    nome = dados["Nome"]

    if tipo == "estagiário":
        resultado = calculos.calcular_salario_estagiario(dados["Salário Bruto"])
    elif tipo == "clt":
        resultado = calculos.calcular_salario_clt(dados["Salário Bruto"])
    elif tipo == "freelancer":
        resultado = calculos.calcular_salario_freelancer(
            dados["Valor ganho por hora"], dados["Horas Trabalhadas"]
        )

    resultado["Nome"] = nome
    resultado["Tipo"] = tipo
    return resultado


def relatorio(lista):
    print("\n" + "=" * 40)
    print("Relatório de Folha de Pagamento")
    print("=" * 40)

    total_pago = 0
    for f in lista:
        print(f"Nome: {f['Nome']}")
        print(f"Tipo: {f['Tipo']}")
        print(f"Salário Bruto: R$ {f['Salário Bruto']:.2f}")
        print(f"Desconto INSS: R$ {f['Desconto INSS']:.2f}")
        print(f"Desconto IRRF: R$ {f['Desconto IRRF']:.2f}")
        print(f"Salário Líquido: R$ {f['Salário Líquido']:.2f}")
        print("-" * 20)
        total_pago += f["Salário Líquido"]

    print(f"Total pago pela empresa: R$ {total_pago:.2f}")
    print("=" * 40)


def salvar_relatorio(lista):
    print("Executando salvar_relatorio com", len(lista), "funcionários.")
    try:
        with open("relatorio_folha.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("\n" + "=" * 40 + "\n")
            arquivo.write("Relatório de Folha de Pagamento\n")
            arquivo.write("=" * 40 + "\n\n")

            total_pago = 0
            for f in lista:
                arquivo.write(f"Nome: {f['Nome']}\n")
                arquivo.write(f"Tipo: {f['Tipo']}\n")
                arquivo.write(f"Salário Bruto: R$ {f['Salário Bruto']:.2f}\n")
                arquivo.write(f"Desconto INSS: R$ {f['Desconto INSS']:.2f}\n")
                arquivo.write(f"Desconto IRRF: R$ {f['Desconto IRRF']:.2f}\n")
                arquivo.write(f"Salário Líquido: R$ {f['Salário Líquido']:.2f}\n")
                arquivo.write("-" * 20 + "\n")
                total_pago += f["Salário Líquido"]

            arquivo.write("\n")
            arquivo.write(f"Total pago pela empresa: R$ {total_pago:.2f}")
            arquivo.write("\n" + "=" * 40 + "\n")

        print(" Relatório salvo com sucesso em relatorio_folha.txt!")

    except Exception as e:
        print(f" Erro ao salvar o arquivo: {e}")


def main():
    lista_funcionarios = []

    while True:
        print("\n Sistema de Folha de Pagamento")
        print("1- Cadastrar Funcionário")
        print("2- Gerar o Relatório")
        print("3- Salvar o Relatório")
        print("4- Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            dados = cadastro.funcionario()
            if dados:
                funcionario_cadastrado = cadastros_funcionario(dados)
                lista_funcionarios.append(funcionario_cadastrado)
                print("\nFuncionário cadastrado com sucesso!")

        elif opcao == "2":
            if not lista_funcionarios:
                print("\nErro: Nenhum funcionário foi cadastro no sistema.")
            else:
                relatorio(lista_funcionarios)

        elif opcao == "3":
            if not lista_funcionarios:
                print("\nErro: Nenhum funcionário foi cadastrado no sistema.")
            else:
                print("\nSalvando...")
                salvar_relatorio(lista_funcionarios)

        elif opcao == "4":
            print("\nFinalizando.")
            break
        else:
            print("\nOpção inválida!")


if __name__ == "__main__":
    main()
