# 11) Função + Lista – Crie uma função chamada calcular_media(lista_notas). A função deve 
# retornar a média dos valores. 
# No programa principal: 
# • Peça 4 notas ao usuário 
# • Coloque numa lista 
# • Use a função para calcular a média 
# • Exiba o resultado


def calcular_media(lista_notas):
    print("A media dos notas é de {lista_notas}.")
soma = 0
notas_digitadas = []
for i in range(4):
    notas = float(input(f"Didite a {i+1}ª nota: "))
    
    soma += notas
    media = soma / 4
    notas_digitadas.append(media) #append() envia notas para notas_digitadas
    calcular_media(notas_digitadas)
