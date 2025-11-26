# 4) Listas – Com uma lista contendo 8 frutas, peça ao usuário uma fruta e diga se ela está na lista
# usando operador in.

cesta_de_frutas = ("maçã", "banana", "uva", "morango", "laranja", "abacaxi", "manga", "kiwi")

print("="*80)
print("\n==== Lista com 8 frutas ====")
fruta = input("Digite o nome da fruta que você procura: ").title()# .title() irá colocar as primeiras letras de cada palavra maiuscula
print("="*80)

if fruta.lower() in cesta_de_frutas:
    print(f"\nA fruta {fruta} está na cesta de frutas.")
    
else:
    print(f"A fruta {fruta} não foi encontarada!")
