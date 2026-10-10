lista = []
par, impar,num = 0,0,0

for i in range(20):
    num = int(input(f"Digite o {i+1}º número: "))
    lista.append(num)
    if num % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"Quantidade de números pares: {par}")
print(f"Quantidade de números ímpares: {impar}")