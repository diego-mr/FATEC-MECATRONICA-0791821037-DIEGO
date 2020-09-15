#PEDE PARA O USUÁRIO DIGITAR UMA SENHA E VALIDA ELA COM A SENHA SECRETA
senha_secreta = '123456'

#Pede para o suário digitar sua senha
senha = input('informe a senha :')

#verifica se a senha do usuário está correta 
if senha == senha_secreta:
  print('Bem vindo hackerman')
else:
  print('acesso negado')
