matriz = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
lista1 = []
lista2 = []
Vcont = 0

for l in range(2):
    for c in range(10):
        matriz[l][c] = int(input(f'Digite o valor da posição {l},{c}: '))
        Vcont += 1
        if Vcont <= 10:
            lista1.append(matriz[l][c])
        elif Vcont > 10:
            lista2.append(matriz[l][c])

print("A matriz é:", matriz)
print("A lista 1 é:", lista1)
print("A lista 2 é:", lista2)