#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. 
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, 
# e R$ 0,45 para viagens mais longas

km = float(input('Quandos Km desaja percorrer? '))
if km <= 200:
    print('O total percorrido custa R${:.2f}.'.format(km * 0.50))
else:
    print('O total percorrido custa R${:.2f}.'.format(km * 0.45))
    