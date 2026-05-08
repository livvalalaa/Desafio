from cadastro import produtos, lista_produtos


def realizar_venda():
    if not lista_produtos():
        return None

    nome_cliente = input("Nome: ").strip()
    if nome_cliente == "":
        print("Erro: Nome não pode ser vazio!")
        return None

    try:
        indice = int(input("Escolha o produto: "))
        produto_selecionado = produtos[indice]
    except:
        print("Produto inválido!")
        return None

    while True:
        try:
            quantidade = int(input("Quantidade: "))
            if quantidade <= 0:
                print("Erro: quantidade inválida!")
                continue

            if quantidade > produto_selecionado["estoque"]:
                print("Erro: estoque insuficiente!")
                continue
            break

        except:
            print("Erro: digite um número válido!")

    valor_bruto = produto_selecionado["preco"] * quantidade
    desconto = 0

    if quantidade > 10:
        desconto = valor_bruto * 0.05

    valor_final = valor_bruto - desconto

    produto_selecionado["estoque"] -= quantidade

    venda = {
        "cliente": nome_cliente,
        "produto": produto_selecionado["nome"],
        "quantidade": quantidade,
        "valor_bruto": valor_bruto,
        "desconto": desconto,
        "valor_final": valor_final,
    }

    print(f"Venda realizada com sucesso! Total: R$ {valor_final:.2f}\n")

    return venda
