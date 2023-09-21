# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar

mercadoria = float(input('Qual o preço da mercadoria? '))
desconto = int(input('Quanto e o percentual de desconto? '))
valor_desconto = mercadoria * desconto / 100
valor_pagar = mercadoria - valor_desconto
print('O desconto e de R${}, o valor a se pagar e de R${},'.format(valor_desconto,valor_pagar ))