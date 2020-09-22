#Exercício 1 Aula 05
#ler 3 valores e encontrar o maior, menor e a média deles.

valor_1 = int(input('informe um valor :'))
valor_2 = int(input('informe outro valor :'))
valor_3 = int(input('informe um terceiro valor :'))

#Encontrar o maior valor 
if valor_1 >= valor_2 and valor_1 >= valor_3:
  maior = valor_1
elif valor_2 >= valor_1 and valor_2 >= valor_3:
  maior = valor_2
else:
  maior = valor_3
print('maior valor :', maior)
#Encontrar o menor valor
if valor_1 <= valor_2 and valor_1 <= valor_3:
  menor = valor_1
elif valor_2 <= valor_1 and valor_2 <= valor_3:
  menor = valor_2
else:
  menor = valor_3
print('menor valor :', menor)

#encontrar a média 

media = (valor_1 + valor_2 + valor_3) / 3
print('valor médio :', media)
