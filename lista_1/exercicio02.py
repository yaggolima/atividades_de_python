import math

def calcular_area_circulo(raio):
    pi= math.pi
    res= pi * (raio**2)

    return res


raio_user= float(input("Digite o valor do raio do circulo: "))
                       
resp = calcular_area_circulo(raio_user)

print(f"A area do circulo é de: {resp:.2f}")