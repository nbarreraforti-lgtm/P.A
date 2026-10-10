lista = []
media = 0
for i in range(20):
    lista.append(int(input(f"Digite o {i+1}º número: ")))
    media += lista[i]
media = media / 20

for i in range(20):
    if lista[i] > media:
        print(f"O número {lista[i]} é maior que a média {media}.")