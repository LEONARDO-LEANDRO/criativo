#Conceitos D: < 3
#Conceitos C: < 6
#Conceitos B: < 8
#Conceitos A: < 10

#Receber sua nota
nota = float(input('Digite aqui a sua nota:'))

#Bloco de Decisões

if(nota <= 3):
    print('Seu conceito é D')
elif(nota <= 6):
    print('Seu conceito é C')
elif(nota <= 8):
    print('Seu conceito é B')
else:
    print('Seu conceito é A')