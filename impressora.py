class Documento:
    def __init__(self, titulo, conteudo):
        self.__titulo = titulo
        self.__conteudo = conteudo

    def get_titulo(self):
        return self.__titulo
    
    def get_conteudo(self):
        return self.__conteudo
    
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_conteudo(self, conteudo):
        self.__conteudo = conteudo

class Impressora:
    def imprimir(self, documento):
        print("\n===Impressão do documento===\n")
        print(f"Titulo: {documento.get_titulo()}")
        print(f"Conteudo: {documento.get_conteudo()}")
        print("==================================")

def main():
    documentos = []
    impressora = Impressora()

    while True:
        print("\n===Menu da Impressora===\n")
        print("1. Criar novo documento")
        print("2. Listar documentos")
        print("3. Imprimir documento")
        print("4. Sair")

        opcao = input("\nDigite a opção que deseja realizar: ")
        if opcao == "1":
            titulo = input("Digite o titulo do documento: ")
            conteudo = input("Digite o conteudo do documento: ")

            doc = Documento(titulo, conteudo)
            documentos.append(doc)
            print(f"\nDocumento criado com sucesso.\n")

        elif opcao == "2":
            if not documentos:
                print("\nNehnum documento criado ainda.\n")
            else:
                print("\n===Lista de documentos===")
            for i, doc in enumerate(documentos):
                print(f"{i + 1}. {doc.get_titulo()}")

        elif opcao == "3":
            if not documentos:
                print("\nNenhum documento diponivel para impressão.\n")
            else:
                print("\nEscolha o número do documento para imprimir: \n")
                for i, doc in enumerate(documentos):
                    print(f"{i + 1}. {doc.get_titulo()}")

                escolha = input("Número: ")
                if escolha.isdigit():
                    escolha = int(escolha)
                    if 1 <= escolha <= len(documentos):
                        impressora.imprimir(documentos[escolha-1])
                    else:
                        print("\nNúmero inválido.\n")
                else:
                    print("\n\nEntrada inválida. Digite um número.")
        
        elif opcao == "4":
            print("Fechando programa...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()