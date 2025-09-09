class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("\nNenhum funcionário neste departamento.\n")
        else:
            for funcionario in self.funcionarios:
                print(f"\n{funcionario.nome} - R$ {funcionario.salario:.2f}")

    def media_salarial(self):
        if not self.funcionarios:
            return 0
        else:
            media = 0
            for funcionario in self.funcionarios:
                media += funcionario.salario
            return media / len(self.funcionarios)


def main():
    funcionarios = []
    departamentos = []

    while True:
        print("\n===MENU===\n")
        print("1. Criar funcionário")
        print("2. Criar departamento")
        print("3. Adicionar funcionário a um departamento")
        print("4. Listar funcionários de um departamento")
        print("5. Mostrar média salarial de um departamento")
        print("6. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("\nDigite o nome do funcionario: ")
            salario = float(input("Digite o salário do funcionario: "))
            # funcionario = Funcionario(nome, salario)
            funcionarios.append(Funcionario(nome, salario))
            print("\nFuncionário criado.\n")

        elif opcao == "2":
            nome = input("\nDigite o nome do departamento: ")
            departamentos.append(Departamento(nome))
            print("\nDepartamento criado.\n")

        elif opcao == "3":
            if funcionarios and departamentos:
                print("\nFucnionários: ")
                for i, f in enumerate(funcionarios):
                    print(f"{i + 1}. {f.nome}")
                i_func = int(input("\nEscolha o o número do funcionário: ")) - 1

                print("\nDepartamentos: ")
                for j, d in enumerate(departamentos):
                    print(f"{j + 1}. {d.nome}")
                j_dep = int(input("\nEscolha o o número do departamento: ")) - 1

                departamentos[j_dep].adicionar_funcionario(funcionarios[i_func])
                print("\nFuncionário adicionado ao departamento\n")

            else:
                print("\nCrie funcionários e departamentos primeiro.\n")

        elif opcao == "4":
                print("\nDepartamentos: ")
                for j, d in enumerate(departamentos):
                    print(f"{j + 1}. {d.nome}")
                j_dep = int(input("\nEscolha o o número do departamento: ")) - 1

                departamentos[j_dep].listar_funcionarios()

        elif opcao == "5":
                print("\nDepartamentos: ")
                for j, d in enumerate(departamentos):
                    print(f"{j + 1}. {d.nome}")
                j_dep = int(input("\nEscolha o o número do departamento: ")) - 1

                media = departamentos[j_dep].media_salarial()
                print(f"\nMédia salarial do departamento {departamentos[j_dep].nome}: R${media:.2f}\n")

        elif opcao == "6":
            print("\nFechando programa...\n")
            break

        else:
            print("\nOpção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()