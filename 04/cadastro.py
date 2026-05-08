produtos = []


def cadastro_produto():
    print("Cadastro Produto:")

    nome = input("Nome: ").strip()
    if nome == "":
        print("Erro: Nome não pode ser vazio!")
        return True

    for p in produtos:
        if p["nome"].lower() == nome.lower():
            print("Erro: Produto já existe na lista!")
            return None

    try:
        preco = float(input("Preço: "))
        if preco <= 0:
            print("Erro: Preço deve ser um número maior que zero!")
            return None

        estoque = int(input("Estoque Inicial: "))
        if estoque < 0:
            print("Erro: Estoque deve ser um número maior que zero!")
            return None

    except:
        print("Erro: Entrada inválida!")
        return None

    produtos.append({"nome": nome, "preco": preco, "estoque": estoque})

    print("Produto cadastrado com sucesso!")


def lista_produtos():
    if not produtos:
        print("Nenhum produto foi cadastrado.")
        return False

    print("Produtos:")
    for i, p in enumerate(produtos):
        print(f"{i} - {p['nome']} | R${p['preco']} | Estoque {p['estoque']}")
    return True
