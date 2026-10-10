
import random


lista = []
numaleatorio = 0
num = 0

for i in range(20):
    numaleatorio = random.randint(1, 50)
    lista.append(numaleatorio)
for i in range(20):
    num = int(input("Digite um número:"))
    if num in lista:
        print("O número está na lista")
    else:
        print("O número não está na lista")