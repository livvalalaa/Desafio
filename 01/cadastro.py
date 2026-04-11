def funcionario():
    print("Cadastro Funcionário:")

    nome = str(input("Nome: ")).strip()
    if nome == "":
        print("Erro: Nome não pode ser vazio!")
        return None

    print("1- Estagiário")
    print("2- CLT")
    print("3- Freelancer")
    tipo = input("Selecione o seu cargo(1, 2, 3): ")

    try:
        if tipo == "1":
            salario_bruto = float(input("Salário: "))
            if salario_bruto <= 0:
                print("Erro: Salário deve ser um número maior que zero!")
                return None
            return {
                "Nome": nome,
                "Tipo": "estagiário",
                "Salário Bruto": salario_bruto,
            }

        elif tipo == "2":
            salario_bruto = float(input("Salário: "))
            if salario_bruto <= 0:
                print("Erro: Salário deve ser um número maior que zero!")
                return None
            return {
                "Nome": nome,
                "Tipo": "clt",
                "Salário Bruto": salario_bruto,
            }

        elif tipo == "3":
            valor_hora = float(input("Valor ganho por hora: "))
            hora_trabalhada = float(input("Horas trabalhadas: "))
            if valor_hora <= 0 or hora_trabalhada <= 0:
                print("Erro: Os valores devem ser maiores que 0!")
                return None
            return {
                "Nome": nome,
                "Tipo": "freelancer",
                "Valor ganho por hora": valor_hora,
                "Horas Trabalhadas": hora_trabalhada,
            }

    except ValueError:
        print("Erro: Digite números em vez de letras!")
        return None
