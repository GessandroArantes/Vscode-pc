#Simulador de Empréstimo Bancário

print("====SISTEMA DE ANALISE DE CRÉDITO====")
nome = input("Nome do Cliente: ")
renda = float(input("Informe sua renda mensal do cliente: (R$) "))
valor_pedido = float(input("Informe o valor do empréstimo desejado: (R$) "))
parcelas = int(input("Informe o número de parcelas: "))
historico = input("Possui nome sujo? (Sim/Não): ")

#Calculo do valor da parcela
valor_parcela = valor_pedido / parcelas

#Exibe um resumo inicial do cliente
print(f"\nCliente: {nome}")
print(f"Valor do Empréstimo: R$ {valor_pedido:.2f}")
print(f"Parcelas: {parcelas}x de R$ {valor_parcela:.2f}")

# Veritica primeiro se o nome está limpo
if historico.lower() == "sim":
    print("Empréstimo negado. Nome com restrição.")
else:
    # Verifica se a parcela não ultrapassa 30% da renda mensal
    if valor_parcela > renda * 0.3:
        print("Empréstimo negado. Parcela excede 30% da renda mensal.")
    else:
        #Verifica o valor do empréstimo em relação à renda
       if valor_pedido > renda * 20:
              print("Empréstimo negado. Valor solicitado muito alto para a renda informada.")
       elif renda >= 5000 and valor_pedido <= 10000:
                print("Empréstimo aprovado com taxa reduzida! Cliente perfil premium.")
       elif renda >= 3000 and valor_pedido < 5000:
                print("Empréstimo aprovado com taxa padrão.")
       else: 
                print("Empréstimo aprovado com taxa elevada (cliente de risco).")
    
    print("\n======ANALISE CONCLUÍDA======")