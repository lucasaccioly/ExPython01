numeros = []
for i in range(3):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)
numeros_ordenados = sorted(numeros)
print("Números em ordem crescente:")
for numero in numeros_ordenados:
    print(numero, end=" ")