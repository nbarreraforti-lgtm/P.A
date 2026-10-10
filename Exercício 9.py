lista = []
soma10, soma20, soma30 = 0, 0, 0
for i in range(10):
    lista.append(int(input(f"Digite o {i+1}º número: ")))
    if lista[i] < 20:
        soma10 += lista[i]
    elif lista[i] >= 20 and lista[i] < 30:
        soma20 += lista[i]
    else:
        soma30 += lista[i]

print(f"A soma dos números menores que 20 é: {soma10}")
print(f"A soma dos números entre 20 e 30 é: {soma20}")  
print(f"A soma dos números maiores que 30 é: {soma30}")