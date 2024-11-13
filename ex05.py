import math

def calcular_delta(a, b, c):
    return b**2 - 4*a*c

def encontrar_raizes(a, b, c):
    delta = calcular_delta(a, b, c)
    if delta < 0:
        print("A equação não possui raízes reais.")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("x1 =", x1)
        print("x2 =", x2)

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

encontrar_raizes(a, b, c)