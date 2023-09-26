#Escreva um programa que leia dois números e que pergunte qualo peração você deseja realizar. 
# Você deve poder calcular a soma (+), subtração (-),multiplicação (*) e divisão (/). 
# Exiba o resultado da operação solicitada

op = input('Qual operação deseja fazer?\n(+)Soma \n(-)Subtração \n(*)Multiplicação \n(/)Divisão \n')
valor1 = float(input('Digite o primeiro valor: ')) 
valor2 = float(input('Digite o segundo valor: ')) 

if op == '+':
    print('{:.2f} + {:.2f} = {:.2f}'.format(valor1, valor2, valor1 + valor2))
    
elif op == '-':
    print('{:.2f} - {:.2f} = {:.2f}'.format(valor1, valor2, valor1 - valor2))
        
elif op == '*':
    print('{:.2f} x {:.2f} = {:.2f}'.format(valor1, valor2, valor1 * valor2))

elif op == '/':
    print('{:.2f} / {:.2f} = {:.2f}'.format(valor1, valor2, valor1 / valor2))
    
else:
    print('Operação inválida')    