# Escreva um programa que calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = int(input('Qual a distância que vai percorrer ? '))
velociade_media = int(input('Qual a velocidade media? '))
tempo_viagem = distancia / velociade_media
print('O tempo de viagem e de aproximadamente {:.2f} horas.'.format(tempo_viagem))