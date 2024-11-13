clientes_feminino = []
clientes_masculino = []
def receber_dados_cliente():
    nome = input("Digite o nome do cliente: ")
    sexo = input("Digite o sexo do cliente (M para masculino, F para feminino): ").upper()
    idade = int(input("Digite a idade do cliente: "))
    return nome, sexo, idade
while len(clientes_feminino) + len(clientes_masculino) < 10:
    nome, sexo, idade = receber_dados_cliente()
    if sexo == 'F':
        clientes_feminino.append({'nome': nome, 'sexo': sexo, 'idade': idade})
    elif sexo == 'M':
        clientes_masculino.append({'nome': nome, 'sexo': sexo, 'idade': idade})
    else:
        print("Sexo inválido. Por favor, digite M para masculino ou F para feminino.")
print("Clientes do sexo feminino:")
for cliente in clientes_feminino:
    print(cliente)
    print("\nClientes do sexo masculino:")
for cliente in clientes_masculino:
    print(cliente)