lista = []
somaP, somaU = 0, 0
for i in range(10):
    lista.append(int(input(f"Digite o {i+1}º número: ")))
    if i < 5:
        somaP += lista[i]
    else:
        somaU += lista[i]
mediaU = somaU / 5
mediaP = somaP / 5
print(f"A média dos 5 primeiros números é: {mediaP}")
print(f"A média dos 5 últimos números é: {mediaU}")
