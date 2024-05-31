import random

#Crie uma função chamada escolher_palavra que retorna uma palavra aleatória de uma lista de palavras.
def escolher_palavra():
    palavras = ['algoritmo', 'framework', 'blockchain', 'api', 'automaçao', 'devops', 'cibersegurança', 'Containerizaçao', 'microserviços', 'chatbots']
    return random.choice(palavras)
 
#Crie uma função chamada exibir_forca que recebe o número de tentativas como parâmetro e imprime o estado atual da forca com base nesse número.
def exibir_forca(tentativas):
        if tentativas == 0:
            print()
            print("|----- ")
            print("|    | ")
            print("|      ")
            print("|      ")
            print("|      ")
            print("|      ")
            print("_      ")
            print()
        elif tentativas == 1:
            print()
            print("|----- ")
            print("|    | ")
            print("|    O ")
            print("|      ")
            print("|      ")
            print("|      ")
            print("_      ")
            print()
        elif tentativas == 2:
            print()
            print("|----- ")
            print("|    | ")
            print("|    O ")
            print("|    | ")
            print("|    | ")
            print("|      ")
            print("_      ")
            print()
        elif tentativas == 3:
            print()
            print("|----- ")
            print("|    | ")
            print("|    O ")
            print("|   /| ")
            print("|    | ")
            print("|      ")
            print("_      ")
            print()
        elif tentativas == 4:
            print()
            print("|----- ")
            print("|    | ")
            print("|    O ")
            print("|   /|\\ ")
            print("|    | ")
            print("|      ")
            print("_      ")
            print()
        elif tentativas == 5:
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
    print()


letras_palavra_secreta = []

#Crie uma função chamada jogar que:
def jogar():
    #Escolhe uma palavra usando a função escolher_palavra.
    palavra_secreta = escolher_palavra()
    
    #Cria uma lista para representar a palavra oculta com sublinhados
    letras_palavra_secreta = ['_'] * len(palavra_secreta)
    
    #Mantém o controle das tentativas e das letras tentadas.
    tentativas = 0
    letras_tentadas = []
    
    #Exibe uma mensagem de boas-vindas e o estado inicial do jogo.
    titulo("Bem-vindo, ao jogo da Forca!")
    print(f"A palavra contém, {len(palavra_secreta)}, letras:")
    print(' '.join(letras_palavra_secreta))
    exibir_forca(tentativas)

    #Dentro da função jogar, crie um loop while que:
    while tentativas < 6:
        
        #Dentro da função jogar, crie um loop while que:        
        letra = input("\nDigite uma letra: ").lower()
        
        #Verifica se a letra já foi tentada.
        if letra in letras_tentadas:
            print("Você já tentou esta letra.")
            continue
        
        letras_tentadas.append(letra)
        
        #Atualiza a lista da palavra oculta se a letra estiver na palavra.
        if letra in palavra_secreta:
            print("Acertou!")
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    letras_palavra_secreta[i] = letra
        else:
            print("Errou!")
            
            #Incrementa o número de tentativas se a letra não estiver na palavra.
            tentativas += 1
        
        #Exibe o estado atual da forca e da palavra oculta.  
        exibir_forca(tentativas)
        print(' '.join(letras_palavra_secreta))
        
        #Verifique se o jogador adivinhou todas as letras da palavra e exiba uma mensagem de vitória.
        if '_' not in letras_palavra_secreta:
            titulo("Parabéns, você acertou a palavra!")
            break
    
    #Verifique se o jogador cometeu 6 erros e exiba uma mensagem de derrota com a palavra correta.    
    if '_' in letras_palavra_secreta:
        titulo(f"Infelizmente, você perdeu! A palavra correta é {palavra_secreta}.")
        
    #No final da função jogar, exiba uma mensagem final agradecendo o jogador por jogar.
    titulo("Obrigada por jogar!")
        
def main():
    jogar()
    
if __name__ == '__main__':
    main()