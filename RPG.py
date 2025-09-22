class Personagem:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel

    def atacar(self):
        print(f"\n{self.nome}, realizou um ataque genérico.\n")

class Guerreiro(Personagem):
    def __init__(self, nome, nivel, forca):
        super().__init__(nome, nivel)
        self.forca = forca

    def atacar(self):
        print(f"\n{self.nome}, realizou um ataque de força bruta de {self.forca} de dano.\n")

class Mago(Personagem):
    def __init__(self, nome, nivel, mana):
        super().__init__(nome, nivel)
        self.mana = mana

    def atacar(self):
        print(f"\n{self.nome}, realizou um ataque mágico de {self.mana} de dano.\n")

def main():
    pers = Personagem("Carlos", 12)
    guerr = Guerreiro("Davi", 17, 35)
    mago = Mago("Julia", 15, 60)

    lista_personagens = [pers, guerr, mago]
    print("---Ação dos Personagens---")
    for p in lista_personagens:
        p.atacar()

    '''
    pers.atacar()
    guerr.atacar()
    mago.atacar()
    '''

if __name__ == "__main__":
    main()