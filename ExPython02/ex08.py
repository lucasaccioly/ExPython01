salarios = {
    'Gerente': 8500.00,
    'Analista': 5000.00,
    'Suporte': 3000.00
}
salarios['Gerente'] *= 1.12
salarios['Analista'] *= 1.12
salarios['Suporte'] *= 1.15
print("Novos salários após o reajuste:")
for cargo, salario in salarios.items():
    print(f"{cargo}: R$ {salario:.2f}")