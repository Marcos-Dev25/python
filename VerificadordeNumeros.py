n = int(input("Digite um número: "))
def verificar_numero(numero):
    if numero %2 == 0:
        return True
    else:
        return False

if verificar_numero(n):
    print("É par")
else:
    print("É ímpar")
