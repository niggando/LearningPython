def eh_incognita(valor):
    try:
        float(valor)
        return False
    except ValueError:
        return True

# Criando um dicionário de operações opostas
operacoes_opostas = {
    "+":"-",
    "-":"+",
    "*":"/",
    "/":"*"
}

# V = D / T
# [+, -, *, /]
# A ideia do projeto é ler uma string, identificar a incógnita e resolvê-la
# Projeto proposto pelo Canal do Youtube - Programação Dinâmica
def operar(formula):
    # Encontrar o "=" e dividir a equação em duas partes
    partes = formula.split("=")
    # encontrar o operador no lado direito
    expressao = partes[1]
    operacoes_validas = ['+', '-', '*', '/']
    for op in operacoes_validas:
        valores = expressao.split(op)
        if len(valores) > 1:
            # encontramos o operador
            operador = op
            break
    # Removendo espaços na expressão e passando para a mesma lista
    valores = [v.strip() for v in valores]
    # Removendo espaços no lado esquerdo (incógnita)
    valore = partes[0].strip()
    # decidir que operação será feita
    # V = D / T
    if eh_incognita(valore):
        A = float(valores[0])
        B = float(valores[1])
    elif eh_incognita(valores[0]):
        A = float(valore)
        B = float(valores[1])
        op = operacoes_opostas[op]
    elif eh_incognita (valores[1]):
        if op == '/' or op == '-':
            A = float(valores[0])
            B = float(valore)
        else:
            op = operacoes_opostas[op]
            A = float(valore)
            B = float(valores[0])
    # retornar o valor da operação
    if op == '+':
        return A + B
    elif op == '-':
        return A - B
    elif op == "*":
        return A * B
    else:
        return A / B

if __name__ == '__main__':
    print(operar("8 = D - 2"))