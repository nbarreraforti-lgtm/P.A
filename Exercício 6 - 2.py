matriz = []
lista = []
comparacao = []
nummatriz, numlista, vcont = 0, 0, 0

for l in range(5):
    for c in range(5):
        nummatriz = int(input(f'Digite um valor para a matriz na posição {l},{c}: '))
        matriz.append(nummatriz)

for l in range(6):
        numlista = int(input(f'Digite um valor para a lista na posição {l}: '))
        lista.append(numlista)

for l in range(5):
    for c in range(5):
        if matriz[l * 5 + c] in lista:
            comparacao.append(matriz[l * 5 + c])
            vcont += 1

print(f'Os valores da matriz que estão na lista são: {comparacao}')
print(f'A quantidade de valores da matriz que estão na lista é: {vcont}')