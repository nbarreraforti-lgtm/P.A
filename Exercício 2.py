Vnum, Vcont, Vnumpositivo = 0,0,0
Vlista = [ ]

for i in range(20):
    Vlista.append(int(input(f"Digite o primeiro {i+1}° número:")))
    
for i in range(20):

    if Vlista[i] > 0:            
      Vnum += Vlista[i] 
    else: 
        Vcont+=1

print("A quantidade de números negativos é:",Vcont)

print("A soma dos números positivos é: ",Vnum)



