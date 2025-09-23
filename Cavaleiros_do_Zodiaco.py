class Personagem:
    def __init__(self, nome, constelacao):
        self.nome = nome
        self.constelacao = constelacao

    def apresentar(self):
        print(f"\nEu sou {self.nome}, cavaleiro de {self.constelacao}")

class CavaleiroDeBronze(Personagem):
    def __init__(self, nome, constelacao, poder_de_luta):
        super().__init__(nome, constelacao)
        self.poder_de_luta = poder_de_luta

    def golpe_especial(self):
        print(f"{self.nome} usou golpe especial com poder de luta de: {self.poder_de_luta}!")

class CavaleiroDeOuro(Personagem):
    def __init__(self, nome, constelacao, casa_do_zodiaco):
        super().__init__(nome, constelacao)
        self.casa_do_zodiaco = casa_do_zodiaco

    def defender_casa(self):
        print(f"{self.nome} defende a casa de: {self.casa_do_zodiaco}.")

class CavaleiroHibrido(CavaleiroDeBronze, CavaleiroDeOuro):
    def __init__(self, nome, constelacao, poder_de_luta, casa_do_zodiaco):
        #super().__init__(nome, constelacao, poder_de_luta)
        CavaleiroDeOuro.__init__(self, nome, constelacao, casa_do_zodiaco)
        self.poder_de_luta = poder_de_luta

    def golpe_especial(self):
        print(f"{self.nome} relealiza um golpe híbrido, com poder de luta: {self.poder_de_luta}!")

    def defender_casa(self):
        print(f"{self.nome} protege a casa de: {self.casa_do_zodiaco}.")
        
def main():
    personagens = []
    while True:
        print("\n===MENU===\n")
        print("1. Cadastrar cavaleiro.")
        print("2. Listar personagens.")
        print("3. Executar golpes especiais ou defesas.")
        print("4. Encerrar programa.")

        opcao = input("\nEscolha uma opção(1-5): ")
        if opcao == "1":
            print("\nTipo de cavaleiro: ")
            print("\n1. Cavaleiro de Bronze.")
            print("2. Cavaleiro de Ouro.")
            print("3. Cavaleiro híbrido.")
            tipo = input("\nEscolha um tipo: ")
            if tipo == "1":
                nome = input("\nNome: ")
                constelacao = input("Constelação: ")
                poder_de_luta = input("Qual o poder de luta: ")
                personagem = CavaleiroDeBronze(nome, constelacao, poder_de_luta)

            elif tipo == "2":
                nome = input("\nNome: ")
                constelacao = input("Constelação: ")
                casa_do_zodiaco = input("Qual a casa do zodiaco: ")
                personagem = CavaleiroDeOuro(nome, constelacao, casa_do_zodiaco)

            elif tipo == "3":
                nome = input("\nNome: ")
                constelacao = input("Constelação: ")
                poder_de_luta = input("Qual o poder de luta: ")
                casa_do_zodiaco = input("Qual a casa do zodiaco: ")
                personagem = CavaleiroHibrido(nome, constelacao, poder_de_luta, casa_do_zodiaco)

            else:
                print("\nTipo inválido.\n")
                continue

            personagens.append(personagem)
            print("\nCavaleiro cadastrado com sucesso.\n")

        elif opcao == "2":
            if not personagens:
                print("\nNenhum cavaleiro cadastrado.\n")
            else:
                print("\n---Cavaleiros---")
                for p in personagens:
                    p.apresentar()

        elif opcao == "3":
            if not personagens:
                print("\nNenhum cavaleiro adicionado.\n")
            else:
                print("\n---Habilidades---")
                for p in personagens:
                    print(f"\n{p.nome}")
                    if isinstance(p, CavaleiroDeBronze):
                        p.golpe_especial()
                    if isinstance(p, CavaleiroDeOuro):
                        p.defender_casa()
                    
        elif opcao == "4":
            print("\nEncerrando programa...\n\n")
            break

        else:
            print("Opção inválida. Digite um número de 1 a 5.")
                    
                        


if __name__ == "__main__":
    main()