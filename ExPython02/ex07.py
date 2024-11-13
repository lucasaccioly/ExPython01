import math

def calcular_area_circunferencia(raio):
    return math.pi * raio**2

raio = float(input("Digite o valor do raio da circunferência: "))
area = calcular_area_circunferencia(raio)
print("A área da circunferência é:", area)