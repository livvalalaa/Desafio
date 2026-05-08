import cadastro
import venda


def relatorio(lista_vendas):
    print("\n" + "=" * 40)
    print("Relatório de Vendas")
    print("=" * 40)

    total = 0

    for v in lista_vendas:
        print(f"Cliente: {v['cliente']}\n")
        print(f"Produto: {v['produto']}\n")
        print(f"Quantidade: {v['quantidade']}\n")
        print(f"Valor Bruto: R$ {v['valor_bruto']:.2f}\n")
        print(f"Desconto: R$ {v['desconto']:.2f}\n")
        print(f"Valor Final: R$ {v['valor_final']:.2f}\n")
        print("-" * 20)

        total += v["valor_final"]

    print(f"Total arrecadado pela loja: R$ {total:.2f}")
    print("-" * 40)


def salvar_relatorio(lista_vendas):
    try:
        with open("relatorio_folha.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("\n" + "=" * 40 + "\n")
            arquivo.write("Relatório de Vendas\n")
            arquivo.write("=" * 40 + "\n\n")

            total = 0

            for v in lista_vendas:
                arquivo.write(f"Cliente: {v['cliente']}\n")
                arquivo.write(f"Produto: {v['produto']}\n")
                arquivo.write(f"Quantidade: {v['quantidade']}\n")
                arquivo.write(f"Valor Bruto: R$ {v['valor_bruto']:.2f}\n")
                arquivo.write(f"Desconto: R$ {v['desconto']:.2f}\n")
                arquivo.write(f"Valor Final: R$ {v['valor_final']:.2f}\n")
                arquivo.write("-" * 20 + "\n")

                total += v["valor_final"]

            arquivo.write("\n")
            arquivo.write(f"Total arrecadado pela loja: R$ {total:.2f}")
            arquivo.write("\n" + "=" * 40 + "\n")

        print(" Relatório salvo com sucesso em relatorio_folha.txt!")

    except Exception as e:
        print(f" Erro ao salvar o arquivo: {e}")


def main():
    lista_vendas = []

    while True:
        print("\n Sistema de Vendas")
        print("1- Cadastrar Produto")
        print("2- Realizar Venda")
        print("3- Gerar o Relatório")
        print("4- Salvar o Relatório")
        print("5- Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastros = cadastro.cadastro_produto()
            if cadastros:
                print("\nProduto cadastrado com sucesso!")

        elif opcao == "2":
            venda_realizada = venda.realizar_venda()
            if venda_realizada:
                lista_vendas.append(venda_realizada)

        elif opcao == "3":
            if not lista_vendas:
                print("\nErro: Nenhuma venda foi realizada.")
            else:
                relatorio(lista_vendas)

        elif opcao == "4":
            if not lista_vendas:
                print("\nErro: Nenhuma venda foi realizada.")
            else:
                print("\nSalvando...")
                salvar_relatorio(lista_vendas)

        elif opcao == "5":
            print("\nFinalizando.")
            break
        else:
            print("\nOpção inválida!")


if __name__ == "__main__":
    main()
