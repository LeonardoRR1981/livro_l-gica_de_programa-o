# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. 
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. 
# O valor da prestação mensal não pode ser superior a 30% do salário. 
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

# input com valor da casa, o salario e a quantidade de meses do emprestimo
# prestação não pode ser maior que 30% do salario

valor_casa = float(input('Qual o valor da casa que deseja comprar? '))
meses = int(input('Em quantos meses vai pagar o emprestimo? '))
salario = float(input('Quanto e seu salario? '))

mensalidade = valor_casa / meses

if mensalidade > (salario * 30) / 100:
    print('A mesalidade não pode ser superior a 30% do seu salario, escolha outra opção de pagamento.') 

else:
    print('Você deseja comprar uma casa de R${:.2f}, e pagar em {} mensalidades, o valor de casa mensalidade e de R${:.2f}'.format(valor_casa, meses, valor_casa / meses))