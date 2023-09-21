#Escreva um programa que leia um valor em metros e o exiba con-vertido em milímetros

metros = float(input('Digite o valor a ser convertido: '))

con = (metros * 1000)
print('{}m e igual a {}mm'.format(metros, con))