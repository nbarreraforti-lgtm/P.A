matriz = []
num = 0
soma = 0

for l in range(4):
    for c in range(4):
      matriz.append(int(input(f'Digite um valor para {l},{c}: ')))
      
for l in range(4):
    for c in range(4):
        if l % 2 == 0 and c %2 != 0:
            soma += matriz[l * 4 + c]

print(f'A soma dos valores é {soma}')