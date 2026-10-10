matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = 0

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor para a posição [{i},{j}]: "))
        if j > i:
            soma += matriz[i][j]

print("A soma dos números digitados acima da diagonal principal:", soma)