# Escreva um programa para calcular a redução do tempo de vida de um fumante. 
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# Considere que um fumante perde 10 minutos de vida a cada cigarro,calcule quantos dias de vida um fumante perderá. 
# Exiba o total em dias.

quantidade = int(input('Quantos cigarros você fuma por dia? '))
anos =  int(input('Quantos anos você? '))
total_cigarros = anos * 365 * quantidade
minutos_perdidos = total_cigarros * 10 
dias = minutos_perdidos / (24 * 60)
print(dias)