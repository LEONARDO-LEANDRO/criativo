#Recebendo idade
idade = int (input('Qual a sua idade? '))

#bloco de decisões
if (idade < 13):
    print ('Tu és criança')

elif (idade < 18):
    print ('Você é um adolescente')

elif(idade < 60):
    print ('Você é um adulto')

else:
    print('Você é um idoso')