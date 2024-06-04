class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}
        
    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            print(f"\nO contato {nome} já existe!")
        else:
            self.contatos[nome] = telefone
            print(f"\nO contato {nome} foi adicionado com sucesso!")
            
    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"\nO contato {nome} foi removido com sucesso!")
        else:
            print(f"\nO contato {nome} não foi encontrado!")
            
    def pesquisar_contato(self, nome):
        if nome in self.contatos:
            print(f"""
Contato encontrado: 
Nome: {nome} | Telefone: {self.contatos[nome]}
""")
        else:
            print(f"\nO contato {nome} não foi encontrado!")
            
    def listar_contatos(self):
        if not self.contatos:
            print("\nAgenda está vazia.")
        else:
            for nome, telefone in self.contatos.items():
                print(f"\nNome: {nome} | Telefone: {telefone}")
                
def menu():
    agenda = AgendaTelefonica()
    
    while True:
        print("\n1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Pesquisar Contato")
        print("4. Listar Contatos")
        print("5. Sair do Programa\n")
        
        try:
            opcao = int(input("Digite o número da opção desejada: "))
            
            if opcao == 1:
                nome = input("\nDigite o nome do contato: ")
                telefone = input ("\nDigite o telefone do contato: ")
                agenda.adicionar_contato(nome, telefone)
            elif opcao == 2:
                nome = input("\nDigite o nome do contato: ")
                agenda.remover_contato(nome)
            elif opcao == 3:
                nome = input("\nDigite o nome do contato: ")
                agenda.pesquisar_contato(nome)
            elif opcao == 4:
                agenda.listar_contatos()
            elif opcao == 5:
                print("\nSaindo do programa! Obrigado pela visita!\n")
                break
            else:
                print("\nOpção inválida!\n")
        except:
            opcao_invalida()
            
def opcao_invalida():
    print("\nOpção inválida!\n")
    print(input("Precione enter para voltar ao menu. "))
            
def main():
    menu()

if __name__ == "__main__":
    main()