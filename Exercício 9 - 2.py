matriz = []
matriz2 = []
num1,num2 = 0,0
for l in range(3):  
    for c in range(3):
        num1 = int(input(f'Digite o valor da posição {l},{c} da matriz 1: '))
        matriz.append(num1)

for l in range(3):
    for c in range(3):
        num2 = int(input(f'Digite o valor da posição {l},{c} da matriz 2: '))
        matriz2.append(num2)

for l in range(3):
    for c in range(3):
        if matriz[l * 3 + c] == matriz2[l * 3 + c]:
            print(f'O valor {matriz[l * 3 + c]} foi encontrado na posição {l},{c}')
print("A matriz 1 é:", matriz)
print("A matriz 2 é:", matriz2)