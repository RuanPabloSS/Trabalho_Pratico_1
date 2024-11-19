saida = ''

def adicao(num1, num2):
    return num1 + num2

def subracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Não foi possível realizar a divisão por 0"
    return num1 / num2

def calculadora(num1, num2, operacao):
    resultado = ''

    if operacao == '+' or operacao.lower() == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subtracao':
        resultado = subracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisao':
        resultado = divisao(num1, num2)
    else:
        return "Operação inválida"

    return resultado

while saida.lower() != 'n':

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, / ou o nome da operação): ")

    resultado = calculadora(num1, num2, operacao)

    print(f"Resultado da operação: {resultado}")

    saida = str.lower(input("Deseja continuar? (S/N): "))


 
