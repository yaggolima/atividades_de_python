import math

resp = float(input("Digite um número decimal positivo: "))

raiz = math.sqrt(resp)
vlr_A_cima= math.ceil(raiz)
vlr_A_baixo= math.floor(raiz)

print(f"A raiz quadrada de {resp} é de {raiz:.2f}")
print(f"Valor arredondado pra baixo: {vlr_A_baixo}")
print(f"Valor arredondado pra cima: {vlr_A_cima}")