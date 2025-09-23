class Participante:
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email

    def emitir_certificados(self):
        return f"\n{self._nome}, - Certificado genérico de participação."

    def get_nome(self):
        return self._nome
    
    def get_email(self):
        return self._email

class Aluno(Participante):
    def __init__(self, nome, email, curso):
        super().__init__(nome, email)
        self.__curso = curso

    def get_curso(self):
        return self.__curso

    def emitir_certificados(self):
        return f"\n{self.get_nome()}, - Concluiu o curso de {self.__curso} com sucesso."

class Instrutor(Participante):
    def __init__(self, nome, email, especialidade):
        super().__init__(nome, email)
        self.__especialidade = especialidade

    def get_especialidade(self):
        return self.__especialidade

    def emitir_certificados(self):
        return f"\n{self.get_nome()}, - Participou como palestrante na área de: {self.__especialidade}."

def main():
    participantes = []
    while True:
        print('\n===Menu===\n')
        print("1. Cadastrar participante.")
        print("2. Listar participantes.")
        print("3. Emitir certificados.")
        print("4. Sair")

        opcao = input("\nEscolha uma opção(1-5): ")
        if opcao == "1":  # *** Não está sendo adicionado a lista.
            print("\nCadastrar: ")
            print("1. Aluno.")
            print("2. Instrutor.")
            escolha = input("\nQual deseja cadastrar(1-2): ")
            
            

            if escolha == "1":
                nome = input("\nNome: ")
                email = input("Email: ")
                curso = input("curso: ")
                participantes.append(Aluno(nome, email, curso))
                print("\nAluno cadastrado com sucesso.")
            elif escolha == "2":
                nome = input("\nNome: ")
                email = input("Email: ")
                especialidade = input("Especialidade: ")
                participantes.append(Instrutor(nome, email, especialidade))
                print("\nInstrutor cadastrado com sucesso.")
                                
            else:
                print("\nOpção inválida.\n")

        elif opcao == "2":
            if not participantes:
                print("\nNenhum participante cadastrado.")

            else:
                print("\n===Participantes Cadastrados===\n")
                for p in participantes:
                    if isinstance(p, Aluno):
                        print(f"Tipo: Aluno")
                        print(f"Nome: {p._nome}")
                        print(f"Email: {p._email}")
                        print(f"Curso: {p.get_curso()}")
                    else:
                        print(f"Tipo: Insrutor")
                        print(f"Nome: {p._nome}")
                        print(f"Email: {p._email}")
                        print(f"Curso: {p.get_especialidade()}")
        
        elif opcao == "3":
            if not participantes:
                print("\nNenhum participante cadastrado.")

            else:
                print("===Certificados===")
                for p in participantes:
                    print(p.emitir_certificados())
            
        elif opcao == "4":
            print("\nEncerrando programa...\n\n")
            break

        else:
            print("Opção inválida. Digite um número de 1 a 5.")


if __name__ == "__main__":
    main()