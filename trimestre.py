#Receber a nota

nota1 = float(input('Qual a nota do primeiro trimestre?'))
nota2 = float(input('Qual a nota do segundo trimestre?'))
nota3 = float(input('Qual a nota do terceiro trimestre?'))

media = ((nota1 + nota2 + nota3)/3)

#bloco de Decisões

if (media < 6):
    print ('Reprovado')

else:
    print ('Aprovado')