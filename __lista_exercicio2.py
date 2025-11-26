# 2) Repetição – Peça 5 números ao usuário usando um for e mostre: 
# • A soma total 
# • A média dos números 


soma = 0  #Cria uma variável que começa em zero para acumular os valores digitado pelo usuario.

print("="*50)
print("\n==== CALCULANDO A SOMA E A MÉDIA DOS NÚMEROS DIGITADOS ====")
for i in range(5):
    numeros = float(input(f"Digite o {i+1}° número: "))
    soma += numeros #Cada número digitado é somado
    media = soma / 5

print("="*50,"\n")
print("===RESULTADO===\n")    
print(f"O valor total da soma foi de {soma}.")
print(f"A média dos números foi de {media}.")
print("="*50, "\n")
