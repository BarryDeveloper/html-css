def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero!"

print("Selecione a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

escolha = input("Digite sua escolha (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == '1':
    resultado = soma(num1, num2)
    print("O resultado da soma é:", resultado)
elif escolha == '2':
    resultado = subtracao(num1, num2)
    print("O resultado da subtração é:", resultado)
elif escolha == '3':
    resultado = multiplicacao(num1, num2)
    print("O resultado da multiplicação é:", resultado)
elif escolha == '4':
    resultado = divisao(num1, num2)
    print("O resultado da divisão é:", resultado)
else:
    print("Escolha inválida!")
