# 10) Função – Crie uma função chamada saudar(nome) que receba um nome e exiba:
# Olá, NOME! Seja bem-vindo(a)!
# Chame a função 3 vezes pedindo nomes ao usuário.

print("="*50)
print("\n==== Função de Saudação Personalizada ====")

def saudar(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a).")
    
for i in range(3):
     usuario = input(f"Digite o {i+1}° nome: ").title().strip()# usuario irá receber o nome e enviar para saudar(nome)
     #.title() irá deixar a primeira letra de cada palavra maiuscula e .strip() limpará espaços extras 
     saudar(usuario)#comando para saudar(nome) receber informacao digitada em "usuario"