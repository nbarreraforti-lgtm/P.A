matriz = []
num = 0
pares = 0

for l in range(4):
    for c in range(4):
        num = int(input(f'Digite um valor para {l},{c}: '))
        matriz.append(num)
        if num % 2 == 0:
            pares += num

print(f'A soma dos valores pares é {pares}')