import random

palavras = ['algoritmo', 'framework', 'blockchain', 'api', 'automaçao', 'devops', 'cibersegurança', 'Containerizaçao', 'microserviços', 'chatbots']
ganhou = False

def escolher_palavra(palavras):
    palavra_aleatoria = random.choice(palavras)
    return palavra_aleatoria

def forma(texto):
     print(texto)
    
def exibir_forca():
    for chance in range(1, 7):
        if chance == 1:
            forma("""
          O
""") 
        elif chance == 2:
            forma("""
          O 
          | 
          | 
""") 
        elif chance == 3:
            forma("""
          O 
        \\| 
          | 
""")
        elif chance == 4:
            forma("""
          O 
        \\|/ 
          |  
""")
        elif chance == 5:
            forma("""
          O 
        \\|/ 
          |
         /  
""")
        else:
            forma("""
          O 
        \\|/ 
          |
         / \ 
""")

def titulo(texto):
    linha = '*' * (len(texto))
    print()
    print(linha)
    print(texto)
    print(linha)
    print()

def jogar():
    titulo("JOGO DA FORCA EM PYTHON")
    while True:
        for letras in escolher_palavra(palavras):
            lista_letras = [letras]
            
        
        exibir_forca()
        
        if ganhou:
            print("Parabéns, você acertou a palavra!")
        else:
            print(f"Infelizmente, você perdeu! A palavra correta é {palavras}.")
        
        titulo("Obrigada por jogar!")
        
def main():
    jogar()
    
if __name__ == '__name__':
    main()