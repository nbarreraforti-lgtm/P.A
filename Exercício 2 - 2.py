matriz = []
maior, menor = 0,0

for l in range(5):
    for c in range(5):
        valor = int(input(f'Digite um valor para {l},{c}: '))
        matriz.append(valor)
        if valor > maior:
            maior = valor
        if valor < menor or menor == 0:
            menor = valor

print("O menor valor da matriz é:", menor)
print("O maior valor da matriz é:", maior)