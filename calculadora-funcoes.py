import os

def limpar_tela():
    os.system("cls")

def obter_operador():
    return float(input("\nEscolha: "))

def operacao_soma(numero1,numero2):
    return numero1 + numero2

def operacao_subtracao(numero1,numero2):
    return numero1 - numero2

def operacao_divisao(numero1,numero2):
    return numero1 / numero2

def operacao_multiplicacao(numero1,numero2):
    return numero1 * numero2

status = True

limpar_tela()

while status == True:
    
    print("-----CALCULADORA-----")

    print("[1] - Soma")
    print("[2] - Subtração")
    print("[3] - Divisão")
    print("[4] - Multiplicação")

    operador = obter_operador()

    limpar_tela()
   
    numero1 = int(input("|Digite o primeiro número para operação: "))
    numero2 = int(input("|Digite o segundo número para operação: "))

    if operador == 1:
        resultado1 = operacao_soma(numero1,numero2)
        limpar_tela()
        print(f"|O resultado é: ", resultado1)

    elif operador == 2:
        resultado2 = operacao_subtracao(numero1,numero2)
        limpar_tela()
        print(f"|O resultado é: ", resultado2)

    elif operador == 3:
        resultado3 = operacao_divisao(numero1,numero2)
        limpar_tela()
        print(f"|O resultado é: ", resultado3)

    elif operador == 4:
        resultado4 = operacao_multiplicacao(numero1,numero2)
        limpar_tela()
        print(f"|O resultado é: ", resultado4)

    else:
        limpar_tela()
        print("\nOpção inválida. Escolha entre 1 e 4.")

    continuar = input("\n|Deseja realizar outra operação? [S/N]: ").upper()
    limpar_tela()

    if continuar == "N":
        status = False  
        print("|FIM DO PROGRAMA|")


