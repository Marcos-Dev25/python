def calcular(num1, operador, num2):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero não permitida."
    else:
        return "Operador inválido!"

num1 = float(input("Digite o primeiro número: "))
operador = input("Digite o operador (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

resultado = calcular(num1, operador, num2)
print("O resultado é:", resultado)