import random

palavras = ['algoritmo', 'framework', 'blockchain', 'api', 'automaçao', 'devops', 'cibersegurança', 'Containerizaçao', 'microserviços', 'chatbots']
#ganhou = False

def escolher_palavra():
    palavra_aleatoria = random.choice(palavras)
    return palavra_aleatoria
    
def exibir_forca(chances):
        if chances == 0:
            print()
            print("|----- ")
            print("|    | ")
            print("|      ")
            print("|      ")
            print("|      ")
            print("|      ")
            print("_      ")
            print()
        elif chances == 1:
            print()
            print("|----- ")
            print("|    | ")
            print("|    O ")
            print("|      ")
            print("|      ")
            print("|      ")
            print("_      ")
            print()
        elif chances == 2:
            print()
            print("|----- ")
            print("|    | ")
            print("|    O ")
            print("|    | ")
            print("|    | ")
            print("|      ")
            print("_      ")
            print()
        elif chances == 3:
            print()
            print("|----- ")
            print("|    | ")
            print("|    O ")
            print("|   /| ")
            print("|    | ")
            print("|      ")
            print("_      ")
            print()
        elif chances == 4:
            print()
            print("|----- ")
            print("|    | ")
            print("|    O ")
            print("|   /|\\ ")
            print("|    | ")
            print("|      ")
            print("_      ")
            print()
        elif chances == 5:
            print()
            print("|----- ")
            print("|    | ")
            print("|    O ")
            print("|   /|\\ ")
            print("|    | ")
            print("|   /  ")
            print("_      ")
            print()
        else:
            print()
            print("|----- ")
            print("|    | ")
            print("|    O ")
            print("|   /|\\ ")
            print("|    | ")
            print("|   / \\ ")
            print("_      ")
            print()

def titulo(texto):
    linha = '*' * (len(texto))
    print()
    print(linha)
    print(texto)
    print(linha)

letras_usuarios = []
letras_palavra_secreta = []

def jogar():
    titulo("Bem-Vindo, ao Jogo da Forca!")

    chances = 0

    palavra_secreta = escolher_palavra()

    while True:
        exibir_forca(chances)
        tentativa = input("Digite uma letra: ")

        #Cria uma lista para representar a palavra oculta com sublinhados
        linha = "_" * (len(palavra_secreta))
        letras_palavra_secreta.append(linha)

        #Mantém o controle das tentativas e das letras tentadas
        for letra in str(len(palavra_secreta)):
            if letra == tentativa:
                print(tentativa, end=" ")
            else:
                letras_usuarios.append(tentativa)
                print(letras_palavra_secreta)
                chances += 1
                exibir_forca(chances)

        #if ganhou:
        #    print("Parabéns, você acertou a palavra!")
        #else:
        #    print(f"Infelizmente, você perdeu! A palavra correta é {palavra_secreta}.")
        
        #titulo("Obrigada por jogar!")
        
def main():
    jogar()
    
if __name__ == '__main__':
    main()