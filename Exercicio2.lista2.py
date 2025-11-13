# 2. Peça para o usuário digitar 5 números inteiros, armazenando-os em
# uma tupla.
# Depois:
# ● Mostre todos os números digitados.
# ● Informe o maior e o menor número.
# ● Diga quantas vezes o número 5 apareceu (se apareceu).

numeros=[]
print("Digite 5 números inteiros:")
for i in range(5):# "for= PARA". "i =0,1,2,3,4". "in= verifica valores dentro do range(5)". "range=(i=0; i>=0; i++)"

    num = int(input(f"Digite o {i+1}º número: "))# Coletando os números inteiros
    numeros.append(num)# Adicionando os números na lista
    lista_tupla = tuple(numeros)# Convertendo a lista em tupla
    print("="*50)# Separador visual
    print("\n✅ Análise da Tupla:")
    
    print(f"Números digitados foram: {lista_tupla}")# Mostrando todos os números digitados
    print(f"O maior número é: {max(lista_tupla)}")# Mostrando o maior número
    print(f"O menor número é {min(lista_tupla)}")# Mostrando o menor número
    contagem_5 = lista_tupla.count(5)# Contando quantas vezes o número 5 apareceu
    if contagem_5 > 0: # Verificando se o número 5 apareceu
         print(f"O numero 5 apareceu {contagem_5} vezes")# Mostrando quantas vezes o número 5 apareceu
    else:# Se o número 5 não apareceu
            print("O número 5 nao foi digitado!")# Mostrando que o número 5 não foi digitado
            #nao consegui fazer funcionar de forma que a análise só apareça depois de os 5 números serem digitados
    

