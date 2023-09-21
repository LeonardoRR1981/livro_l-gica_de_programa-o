# Escreva um programa que leia a quantidade de dias, horas, minutose segundos do usuário. Calcule o total em segundos

dias = int(input('Digite os dias '))
horas = int(input('Digite as horas '))
minu = int(input('Digite os minutos  '))
seg = int(input('Digite os segundos '))

total = dias * 24 * 60 * 60 + horas * 3600 + minu * 60 + seg
print(total)