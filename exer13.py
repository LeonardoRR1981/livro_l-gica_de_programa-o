# Escreva um programa que pergunte a velocidade do carro de um usuário. 
# Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.



velocidade = int(input('Qual a velicidade que o caro estava? '))

if velocidade < 80 :
    print('Velocidade permitida.')
if velocidade >= 80:
    multa = (velocidade - 80) * 5
    print('Velocidade permitida ultrapassada, você estava a {}KM, sua multa e de R${}.'. format(velocidade, multa))