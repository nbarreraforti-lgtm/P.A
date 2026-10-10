import random

matriz = []
tentativa = []
Vcont, acerto = 0,0

for l in range(5):
    for c in range(5):
        matriz.append(random.randint(0, 40))

for l in range(5):
    for c in range(5):
        tentativa.append(int(input(f'Digite um valor para a tentativa na posição {l},{c}: ')))


for l in range(5):
    for c in range(5):
        if matriz[l * 5 + c] == tentativa[l * 5 + c]:
            acerto = matriz[l * 5 + c]
            matriz[l * 5 + c] = 0
            Vcont += 1

            print(f'O valor {acerto} foi encontrado na posição {l},{c}')
print("A quantidade de valores encontrados na matriz é:", Vcont)