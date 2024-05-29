import os

def adicionar():
    primeiro_numero = int(input("\nDigite o primeiro número: "))
    segundo_numero = int(input("\nDigite o segundo número: "))
    resultado = primeiro_numero + segundo_numero
    exibir_subtitulo(f"Adição: {primeiro_numero} + {segundo_numero} = {resultado}")
    
def subtrair():
    primeiro_numero = int(input("\nDigite o primeiro número: "))
    segundo_numero = int(input("\nDigite o segundo número: "))
    resultado = primeiro_numero - segundo_numero
    exibir_subtitulo(f"Subtração: {primeiro_numero} - {segundo_numero} = {resultado}")

def multiplicar():
    primeiro_numero = int(input("\nDigite o primeiro número: "))
    segundo_numero = int(input("\nDigite o segundo número: "))
    resultado = primeiro_numero * segundo_numero
    exibir_subtitulo(f"Multiplicação: {primeiro_numero} * {segundo_numero} = {resultado}")
    
def dividir():
    primeiro_numero = int(input("\nDigite o primeiro número: "))
    segundo_numero = int(input("\nDigite o segundo número: "))
    if segundo_numero == 0:
        exibir_subtitulo("Não pode dividir um número por zero.")
    else:
        resultado = float(primeiro_numero / segundo_numero)
        exibir_subtitulo(f"Divisão: {primeiro_numero} / {segundo_numero} = {resultado}")

def menu():
    opcao_escolhida = ''
    while(opcao_escolhida != 5):
        print("""
        CALCULADORA:
        """)
        print()
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair\n")
        
        try:
            opcao_escolhida = int(input("Escolha uma opção: "))
            if opcao_escolhida == 1:
                adicionar()
            elif opcao_escolhida == 2:
                subtrair()
            elif opcao_escolhida == 3:
                multiplicar()
            elif opcao_escolhida == 4:
                dividir()
            elif opcao_escolhida == 5:
                finalizar_programa()
            else:
                opcao_invalida()
        except:
            opcao_invalida()
        
def voltar_ao_menu():
    exibir_subtitulo(input("Precione enter para voltar ao menu. "))
    main()
    
def opcao_invalida():
    exibir_subtitulo("Opção inválida!")
    voltar_ao_menu()
    
def exibir_subtitulo(texto):
    os.system("cls")
    linha = '*' * (len(texto))
    print()
    print(linha)
    print(texto)
    print(linha)
    print()    
    
def finalizar_programa():
    exibir_subtitulo("Obrigada por acessar o programa de calcular.") 
    
def main():
    menu()

if __name__ == "__main__":
    main()