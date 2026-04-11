def calcular_salario_clt(salario_bruto):
    inss = salario_bruto * 0.08
    if salario_bruto >= 2000:
        irrf = salario_bruto * 0.10
    else:
        irrf = 0

    salario_liquido = salario_bruto - inss - irrf
    return {
        "Salário Bruto": salario_bruto,
        "Desconto INSS": inss,
        "Desconto IRRF": irrf,
        "Salário Líquido": salario_liquido,
    }


def calcular_salario_estagiario(salario_bruto):
    return {
        "Salário Bruto": salario_bruto,
        "Desconto INSS": 0.0,
        "Desconto IRRF": 0.0,
        "Salário Líquido": salario_bruto,
    }


def calcular_salario_freelancer(valor_hora, hora_trabalhada):
    salario_bruto = valor_hora * hora_trabalhada
    desconto = salario_bruto * 0.05
    salario_liquido = salario_bruto - desconto
    return {
        "Salário Bruto": salario_bruto,
        "Desconto INSS": desconto,
        "Desconto IRRF": 0.0,
        "Salário Líquido": salario_liquido,
    }
