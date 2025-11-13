# 1. Crie uma tupla chamada nomes com 5 nomes de colegas.
# Depois, exiba:
# ● O primeiro e o último nome da tupla.
# ● A quantidade total de nomes.



nomes = ("João", "Maria", "José", "Carlos", "Eva")# tupla com 5 nomes
print("\n====Lista de Nomes dos Colegas====")
print("="*75)
print(f"Lista de nomes dos colegas:\n{nomes}")# exibindo a lista completa de nomes
print(f"Primeiro nome: {nomes[0]}")# exibindo o primeiro nome
print(f"O ultimo nome é: {nomes[4]}")# exibindo o ultimo nome
print(f"A quantidade de nomes é: {len(nomes)}")# exibindo a quantidade total de nomes
print("="*75)