# 3) Listas – Cadastro Simples (Fácil) 
# Peça nomes ao usuário e adicione em uma lista. 
# O programa deve parar quando o usuário digitar "sair". 
# Ao final, exiba: 
# • Quantos nomes foram cadastrados 
# • A lista completa 

nomes = ()
print("="*90)
print("\n==== DIGITE OS NOMES QUE DESEJA ADICIONAR A LISTA E (sair) PARA ENCERRAR ====")
while True:
 
    cadastro = input("Digite o nome desejado: ").title()# .title() irá colocar as primeiras letras de cada palavra maiuscula

    if cadastro.lower() == 'sair': #.lower() irá colocar todas as letras em minuscula 
      print("Saindo do sistema! Até logo.")
      break
    nomes.append(cadastro)

print(f"Foram adicionaddos {len(cadastro)} nomes.")
print(f"Os nomes digitados foram {nomes}.\n")