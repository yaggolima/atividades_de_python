import math

def calcular_hipotenusa(cateto_a, cateto_b):
    h = math.sqrt(cateto_a**2 + cateto_b**2)
    return h

print("--- Calcular Hipotenusa ---")

a = float(input("Digite o valor do cateto A: "))
b = float(input("Digite o valor do cateto B: "))

resultado = calcular_hipotenusa(a, b)

print(f"O valor da hipotenusa é: {resultado:.2f}")