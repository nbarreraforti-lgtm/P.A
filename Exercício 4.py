matriz = [[0,0,0],[0,0,0],[0,0,0]]
Vcont = 0

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] > 10:
            Vcont += 1

for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]}]', end=' ')
    print()
print(f'Quantidade de valores maiores que 10: {Vcont}')