matriz = []
num = 0
linha = [0,0,0,0,0]
coluna = [0,0,0,0,0]

for l in range(5):
    linha = []
    for c in range(5):
        num = int(input("Digite o número: "))
        linha.append(num)

    matriz.append(linha)

for l in range(5):
    for c in range(5):
        linha[l] += matriz[l][c]
        coluna[c] += matriz[l][c]

    
print(coluna)
print(linha)
        