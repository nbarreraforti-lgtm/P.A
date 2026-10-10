matriz = []
num, ordem = 0, 0
for l in range(4):
    for c in range(4):
        num = int(input(f'Digite o valor da posição {l},{c}: '))
        matriz.append(num)

for l in range(4):
    for c in range(4):
        if matriz[l] > matriz[l + 1]:
            ordem = matriz[l]
            matriz[l] = matriz[l + 1]
            matriz[l + 1] = ordem
print(f"A matriz ordenada é: {matriz}")
