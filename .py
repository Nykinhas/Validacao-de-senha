#Enunciado:
"""
4. Validar senha
Faça um programa que solicite usuário e senha e compare com valores armazenados em
duas variáveis. O programa deve exibir “Acesso negado” caso usuário e/ou senha estejam
errados e “Acesso autorizado”, caso ambos estejam corretos.
"""

#Declaração de variáveis
usuario = "admin"
senha = "123456"

#Entrada de dados
usuario_digitado = input("Digite o usuário: ")
senha_digitada = input("Digite a senha: ")

#Processamento
if usuario_digitado == usuario and senha_digitada == senha:
  print("Acesso autorizado")
else:
  print("Acesso negado")
