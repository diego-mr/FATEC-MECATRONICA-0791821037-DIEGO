#Escreva um programa que, dado o valor de um raio e uma altura, imprima o valor do volume de um cilindro  
valor_raio = float(input('inserir o valor do raio:'))
valor_altura = float(input('inserir o valor da altura:'))
valor_raio_ao_quadrado = valor_raio * valor_raio
valor_volume_do_cilindro = 3.1415926536 * valor_raio_ao_quadrado * valor_altura
print('valor do volume do cilindro =', valor_volume_do_cilindro)
