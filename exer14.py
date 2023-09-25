# Escreva um programa que leia três números e que imprima o maiore o menor.

x = int(input('Escreva um número: '))
y = int(input('Escreva um número: '))
z = int(input('Escreva um número: '))

if x > y and x > z:
    print('{} e maior que {} e {}'.format(x, y, z))
if y > x and y > z:
    print('{} e mai0r que {} e {}'.format(y, x, z))
if z > x and z > y:
    print('{} e maior que {} e {}'.format(z, x, y))        