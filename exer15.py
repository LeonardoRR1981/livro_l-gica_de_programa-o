#Escreva um programa que pergunte o salário do funcionário e calculeo valor do aumento. 
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, de 15%
 
salario = float(input('Qual seu salario? '))
if salario > 1250:
   novo_salario = salario + (salario * 10 ) / 100
   print('Você resebeu um aumento de 10%, seu novo salario e de R${:.2f}.'.format(novo_salario))
   
if salario <= 1250:
   novo_salario = salario + (salario * 15 ) / 100
   print('Você resebeu um aumento de 15%, seu novo salario e de R${:.2f}.'.format(novo_salario))
   
