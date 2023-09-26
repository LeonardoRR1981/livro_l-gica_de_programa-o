# Escreva um programa que calcule o preço a pagar pelo fornecimentode energia elétrica. 
# Pergunte a quantidade de kWh consumida e o tipo de instalação: 
# R para residências, 
# I para indústrias e 
# C para comércios. 
# Calcule o preço apagar de acordo com a tabela a seguir
# Preço por tipo e faixa de consumo:
# Recidencial: ate de 500 kwh, R$ 0,40, acima de 500 kwh, R$ 0.65
# Comercial: ate de 1000 kwh, R$ 0,55, acima de 1000 kwh, R$ 0.60
# Industrial: ate de 5000 kwh, R$ 0,55 acima de 5000 kwh, R$ 0.60

tipo = input('Qual o tipo de intalação?\nAperte: \n(R) Para recidensial. \n(C) Para comercial. \n(I) Para industrial\n ')
quantidade = int(input('Quantos kWh consumiu? '))
if tipo == 'R':
    if quantidade <= 500:
        total = quantidade * 0.40 
        print('Você consumiu {}kWh da intalação residensial, o valor da conta e de R${:.2F}.'.format(quantidade, total))

if tipo == 'R':
    if quantidade > 500:
        total = quantidade * 0.65       
        print('Você consumiu {}kWh da intalação residencial, o valor da conta e de R${:.2F}.'.format(quantidade, total))
             
elif tipo == 'C':
    if quantidade <= 1000:
        total = quantidade * 0.55 
        print('Você consumiu {}kWh da intalação comercial, o valor da conta e de R${:.2F}.'.format(quantidade, total))
        
    if quantidade > 1000:
        total = quantidade * 0.60 
        print('Você consumiu {}kWh da intalação comercial, o valor da conta e de R${:.2F}.'.format(quantidade, total))
        
else:
    if quantidade <= 5000:
        total = quantidade * 0.55 
        print('Você consumiu {}kWh da intalação industrial, o valor da conta e de R${:.2F}.'.format(quantidade, total))
    
    if quantidade > 5000:
        total = quantidade * 0.60
        print('Você consumiu {}kWh da intalação industrial, o valor da conta e de R${:.2F}.'.format(quantidade, total))


