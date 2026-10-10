matriz = []
num = 0

for l in range(4):
    for c in range(4):
        valor = int(input(f'Digite um valor para {l},{c}: '))
        matriz.append(valor)

num = int(input('Digite um valor para ser buscado: '))
for l in range(4):
    for c in range(4):
        if matriz[l * 4 + c] == num:
            print(f'O valor {num} foi encontrado na posição {l},{c}')