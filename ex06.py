def calcular_ano_nascimento(idade_atual, ano_atual):
    return ano_atual - idade_atual

idade_atual = int(input("Digite sua idade atual: "))
ano_atual = int(input("Digite o ano atual: "))

ano_nascimento = calcular_ano_nascimento(idade_atual, ano_atual)
print("Você nasceu aproximadamente no ano de", ano_nascimento)