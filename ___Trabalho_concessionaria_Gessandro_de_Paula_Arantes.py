# =========================================================================================================

#**** Requisitos Técnicos do Sistema:****
# • Cadastro Inicial do Cliente
# → Solicitar nome, telefone e saldo inicial.
# → Armazenar esses dados em um dicionário.

# =========================================================================================================

# 1- Venda de Veículos (Cliente → Empresa)
# • O cliente informa marca e modelo do veículo.
# • O sistema consulta o valor FIPE (armazenado em um dicionário).
# • A proposta da empresa deve ser o valor FIPE com 12% de desconto.
# • Se o cliente aceitar, o valor é adicionado ao saldo e o veículo entra na lista da empresa.
# • Exemplo:
# Valor FIPE: R$ 50.000
# Proposta: R$ 44.000 (–12%)

# =========================================================================================================

# 2- Aluguel de Veículos (Cliente ← Empresa)
# • O cliente escolhe um veículo disponível para locação (lista pré-definida).
# • Informa o número de dias desejado.
# • O valor do aluguel é R$77 por dia.
# • O sistema verifica se o saldo é suficiente e, se confirmado,
# o desconta o valor,
# o remove o veículo da lista de disponíveis.
# • Exemplo:
# Aluguel de 5 dias → 5 × 77 = R$ 385

# =========================================================================================================

# 3 Compra de Veículos (Cliente ← Empresa)
# • O cliente escolhe um veículo da lista de veículos à venda.
# • O sistema consulta o valor FIPE e adiciona 25% de acréscimo.
# • Se o saldo for suficiente, o valor é descontado e o veículo é removido da lista.
# • Exemplo:
# Valor FIPE: R$ 60.000
# Preço de venda: R$ 75.000 (+25%)

# =========================================================================================================

# Regras Gerais:
# • O sistema deve permitir voltar ao menu principal a qualquer momento.
# • Se o saldo for insuficiente, a operação será cancelada automaticamente.
# • Usar um dicionário “tabela FIPE” com pelo menos 5 modelos e valores.
# • Usar funções para cada funcionalidade (vender(), alugar(), comprar(), menu() etc.).
# • Utilizar estrutura de repetição para manter o programa em execução até o usuário escolher “Sair”.

# =========================================================================================================


#NOME DA LOJA
print("="*90,"\n")
print("                          SEJA BEM-VINDO A DREAMS MASTER \n")
print("="*90,"\n")
    
# =========================================================================================================

#CARROS EM ESTOQUE NA LOJA 
#Dicionário / Objeto - onde se encontra o estoque como modelo dos carros e preço fipe. 
estoque_carros = {
     "pulse": 112000.0,
     "t-cross": 118000.0,
     "onix": 68000.0,
     "creta": 135000.0,
     "corolla": 125000.0,
     "hr-v": 122000.0,
     "kwid": 52000.0,
     "ka": 52000.0,
     "kicks": 128000.0,
     "renegade": 115000.0,
     "c4 cactus": 117000.0
}

# =========================================================================================================

#CARROS PARA ALUGUEL
#Lista com tuplas 
carros_aluguel=[
    ("jeep", "renegade"), ("t-cross", "volkswagen"),
     ("chevrolet", "onix"), ("ford", "Ka"), ("renault", "kwid")
]

# =========================================================================================================

#CARROS PARA VENDER
#Lista com tuplas
carros_venda = [
    ("pulse", "fiat"),
    ("t-cross", "volkswagen"),
    ("onix", "chevrolet"),
    ("creta", "hyundai"),
    ("corolla", "toyota"),
    ("hr-v", "honda"),
    ("kwid", "renault"),
    ("ka", "ford"),
    ("kicks", "nissan"),
    ("renegade", "jeep"),
    ("c4 cactus", "citroën")


]

# =========================================================================================================


# PEDINDO AO CLIRNTE QUE DIGITE SEUS DADOS
print("* Por gentileza, prencha as informções a seguir para darmos inicio ao atendimento!\n")
cliente = {
            "nome" : input("Digite seu nome: ").title(),#.title() irá deixar as primeiras letras do nome e sobrenome maiusculas 
            "celular" : input("Número para contato: "),
            "saldo" : float(input("Digite seu saldo inicial R$: "))#float 
}     
print(cliente) 

# =========================================================================================================

#Menu de opçôes
def menu():
    print("\n----ESCOLHA UMA DAS OPÇÕES----\n")
    print("1- VENDER VEÍCULO.\n")
    print("2- ALUGAR VEÍCULO.\n")
    print("3- COMPRAR VEÍCULO.\n")
    print("4- CONSULTAR SALDO.\n")
    print("5- SAIR.\n")
    return menu
# =========================================================================================================

# FUNÇÃO PARA O CLIENTE VENDER O CARRO PESSOAL PARA LOJA

def vender_veiculo():# IRÁ PARA O MENU
    print("="*120)
    print("\n===== VENDA DE VEÍCULO PARA DREAMS MASTER ====\n")
    print("\n====CARROS EM ESTOQUE====\n")
    print(carros_venda)#Pra saber o que tem no estoque
    print("="*120)
    modelo = input("\nDigite o Modelo do seu carro: ").strip().lower()
    #strip() irá remove espaços em branco no início e no fim do que o cliente digitar.
    #lower() irá garantir que todas strings sejam letras minúsculas.
    marca = input(" Digite a Marca do seu carro: ").strip().lower()
    if modelo not in estoque_carros:
       print("Este veículo não se encontra em nosso estoque. Venda não realizada.")
       return
    tabela_fipe = estoque_carros[modelo]
    proposta_loja = tabela_fipe / 0.12
    print(f"O valor da TABELA FIPE é R${tabela_fipe:.2f}") 
    print(f"A Proposta da DREAMS MASTER é R${proposta_loja:.2f}")
    escolha = input("Você aceita a Proposta da Loja? (sim/não): ").lower().strip()
    if escolha == "sim":
       cliente["saldo"] += proposta_loja
       carros_venda.append((modelo, marca))
       print("Venda do veículo realizada com sucesso!")
    else:
        print("Venda cancelada!")
   

# =========================================================================================================

#FUNÇÃO PARA O CLIENTE ALUGAR O CARRO

def alugar_veiculo(): #IRÁ PARA O MENU
    print("\n===== ALUGAR VEÍCULO ====")
    if not carros_aluguel:
         print("Veículo não encontrado. Tente novamente!")
         return #irá fazer a verificação se o veículo está disponivel no estoque
    print("\n==== Veculos disponiveis para aluguel ====")
    for i, carro in enumerate(carros_aluguel):
            print(f"{i+1} - {carro[0]} ({carro[1]})")# Usuário escolhe o carro pelo número
    escolha = input("Digite o número do carro desejado: ")
    if escolha < 0 or escolha >= len(carros_aluguel):
        print("Veículo não encontrado. Tente novamente!")
        return #se o usuario digitar algim numero errado irá retornar à opções novamente
    dias_aluguel = input("Digite a quantidade de dias desejado para aluguel: ")
    carro = carros_aluguel[0][0]#pega posicao do carro na tupla
    preco_dia = carros_aluguel[0][1]#pega posiçaõ do valo da diaria na tupla
    total_aluguel = preco_dia * dias_aluguel
    print(f"O valor total do aluguel ficou por: R${total_aluguel:.2f}")
    if cliente["saldo"] < total_aluguel:
        print("Saldo insuficiente.")
        return
    confirmar = input("Confirmar aluguel? (sim/não): ").lower()
    if confirmar == "sim":
        cliente["saldo"] -= total_aluguel
        carro = carros_aluguel.pop(escolha)
        print(f"Você alugou o veículo '{carro[0]}'.")
    else:
     print("Aluguel cancelado!")     

# =========================================================================================================

#FUNÇÃO PARA O CLIENTE CONPRAR O CARRO

def comprar_veiculo():
    print("\n==== COMPRAR VEÍCULO ====")
    if not carros_venda:
        print("Veículo digitado não disponivel para venda. Tente novamente!")
        return
    print("\n==== Veículos disponiveis para venda ====")
    for i, carro in enumerate(carros_venda):
           print({i+1} - {(carro[0])} ({carro[1]}))
    escolha = int(input("Digite o numero do carro desejado: ")) - 1
    if escolha < 0 or escolha >= len(carros_venda):
       print("Opção inválida!")
       return
    marca = estoque_carros[escolha]['marca']
    modelo = estoque_carros[escolha]['modelo']
    valor_fipe = estoque_carros.get(marca, modelo, 0)

    if valor_fipe == 0:
             print(f"Erro: Preço de referência para '{marca}' não encontrado.")
             return
    valor_total_veiculo = valor_fipe * 0.25   #valor final do veiculo com aumento de 25%
    print(f"VAlor do veículo ficou por: R$ {valor_total_veiculo}")
    if cliente['saldo'] < valor_total_veiculo:
         print("Saldo insufisiente!")
         return
    confirmar = input(f"Deseja finalizar a compra do {marca, modelo} ? (sim,não) ").lower()
    if confirmar == 'sim':
         cliente['saldo'] -= valor_total_veiculo
         carro = carros_venda.pop(escolha)
         print(f"Você comprou o veiculo '{marca, modelo}'.")
    else:
         print("Compra cancelada!")

# =========================================================================================================

#FUNÇÃO PARA O LOOP DO PROGRAMA

while True:
     menu()
     opcao = input("Escolha a opção desejada digitando o número correspondente: ")
     match opcao:
          case "1":
              vender_veiculo()
          case "2":
               alugar_veiculo()
          case "3":
               vender_veiculo()
          case "4":
               print(f"\nSeu saldo atual é: R$ {cliente['saldo']:.2f} reais.")
          case "5":
               print("Saindo do sistema. Até logo!")
               break
          case _:
               print("Opçao invalida! Tente novamente.")
     
          
          
     
                


              
                 
