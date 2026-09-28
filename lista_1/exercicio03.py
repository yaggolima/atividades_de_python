def encontrar_maior(a,b,c):
    num= 0
    if a > b and a > c:
        num= a
    elif b > a and b > c:
        num=b
    elif c > a and c > b:
        num= c

    return num

num_1 = int(input("Digite um número inteiro: "))
num_2= int(input("Digite outro número inteiro: "))
num_3= int(input("Digite outro número inteiro: "))

resp = encontrar_maior(num_1,num_2,num_3)

print(f"O maior numero é esse: {resp}")