vtotnotas,vmedia,vlistanotas=0.0,0.0,[]
for i in range(5):
    vlistanotas.append(int(input(f"Entre com a {i+1}ª nota :")))
    
for i in range(5):
    vtotnotas+=vlistanotas[i]

vmedia=vtotnotas/5
print("A média do aluno é :",vmedia)
if vmedia>=7:
    print("Aluno aprovado !")    
else:
    if vmedia>=5:
        print("Aluno em Recuperação !")    
    else:
        print("Aluno Reprovado !")    
        

        