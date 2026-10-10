Vnum, Vmaior, Vcont = 0,0,0
Vlista = []

for i in range(10):
    Vlista.append(int(input(f"Digite o {i+1}° número: ")))

for i in range(10):

    if Vlista[i] > Vmaior:
        Vmaior = Vlista[i]
        Vcont = i + 1
print ("A posição do maior número é: ",Vcont)

