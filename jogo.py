# 1. DEFINIÇÃO DAS FUNÇÕES
def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    # Verifica divisão por zero usando a condição 'if'
    if num2 == 0:
        return "Erro! Divisão por zero não é permitida."
    return num1 / num2

# 2. INTERFACE E ENTRADA DE DADOS
print("=== CALCULADORA SIMPLES EM PYTHON ===")
print("Selecione a operação:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")
print("====================================")

operacao = input("Digite o número da operação (1/2/3/4): ")

# A função float() permite que o usuário digite números decimais (com ponto)
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
for resultado in [0]:
# 3. LÓGICA DE EXECUÇÃO (USANDO CONDICIONAIS)


 if operacao == '1':
    resultado = somar(num1, num2)
 elif operacao == '2':
    resultado = subtrair(num1, num2)
 elif operacao == '3':
    resultado = multiplicar(num1, num2)
 elif operacao == '4':
    resultado = dividir(num1, num2)
else:
    resultado = "Opção inválida."

# 4. IMPRESSÃO DO RESULTADO
print(f"\nO resultado é: {resultado}")