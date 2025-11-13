# Lista para coletar os números
numeros = []

print("Por favor, digite 5 números inteiros:")

# Loop para coletar 5 números sem validação de erro
for i in range(5):
    # ATENÇÃO: Se o usuário digitar algo que não seja um inteiro, o programa irá parar aqui.
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# CONVERTE A LISTA PARA TUPLA
minha_tupla = tuple(numeros)

# ANÁLISES E EXIBIÇÃO DOS RESULTADOS
print("=" * 50)
print("\n✅ Análise da Tupla:")

# 1. Mostre todos os números digitados.
print(f"Os números digitados na tupla são: {minha_tupla}")

# 2. Informe o maior e o menor número.
print(f"O maior número é: {max(minha_tupla)}")
print(f"O menor número é: {min(minha_tupla)}")

# 3. Diga quantas vezes o número 5 apareceu.
contagem_5 = minha_tupla.count(5)
if contagem_5 > 0:
    print(f"O número 5 apareceu {contagem_5} vezes.")
else:
    print("O número 5 não foi digitado nenhuma vez.")

print("=" * 50)