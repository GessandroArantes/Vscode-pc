# 6) Tupla – Crie uma tupla com números inteiros. Peça ao usuário um número e diga: 
# • Se ele está na tupla 
# • Em qual posição (índice) aparece pela primeira vez 


numeros_inteiro = [35, 7, 12, 21, 41, 56, 68, 59, 74, 92]
print("="*50)
print("\n=== Encontrando número e posição na tupla ====")
numero = int(input("Digite um número para ver se está na tupla: "))

if numero in numeros_inteiro:
 posicao_indice = numeros_inteiro.index(numero)+ 1 #.index() irá identificar a posição do item
 # +1 irá garantir que o índice começará a ser contado do numero 1 e nao 0 
 print(f"Todos números da lista são {numeros_inteiro}.")
 print(f"O número {numero} está na lista.")
 print(f"O número {numero} está na posição (indice): {posicao_indice} da tupla.")
else:
  print("Número não encontrado!") 
  print(f"Todos números da lista são {numeros_inteiro }.") 
  print("="*50)
