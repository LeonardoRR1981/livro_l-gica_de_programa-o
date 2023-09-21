# Escreva uma expressão que será utilizada para decidir se um aluno foiou não aprovado.
# Para ser aprovado, todas as médias do aluno devem ser maioresn que 7.
# Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis:
# matéria1, matéria2 e matéria3.

materia1 = float(input('Difite a nota: '))
materia2 = float(input('Difite a nota: '))
materia3 = float(input('Difite a nota: '))
media = (materia1 + materia2 + materia3) / 3

if (media > 7):
  print('Sua nota e de {:.2}, você passou de ano. Parabens!!!'.format(media))
  
else:
     print('Sua nota e de {:.2}, você não passou de ano, estude mais ano quem vem.'.format(media))