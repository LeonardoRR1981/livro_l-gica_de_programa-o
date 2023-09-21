# Faça um programa que calcule o aumento de um salário. 
# Ele deve solicitar o valor do salário e a porcentagem do aumento. 
# Exiba o valor do aumento e do novo salário.

salario = float(input('Qual e o salario? '))
porcentagem = int(input('Quanto a prcentagem de aumento? '))
novo_salario = salario + (salario * porcentagem) / 100
valor_aumento = novo_salario - salario
print('Seu aumento foi de R${:.2f}, seu novo salario e de R${}'.format(valor_aumento, novo_salario))