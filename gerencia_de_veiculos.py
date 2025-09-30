from abc import ABC, abstractmethod

class VeiculoTransporte(ABC):
    def __init__(self, placa, capacidade_passageiros):
        self.placa = placa
        self.capacidade = capacidade_passageiros

    @abstractmethod
    def calcularCustoOperacional(self):
        pass

class Onibus(VeiculoTransporte):
    def __init__(self, placa, capacidade_passageiros, consumo_km):
        super().__init__(placa, capacidade_passageiros)
        self.consumo_km = consumo_km

    def calcularCustoOperacional(self):
        return self.consumo_km * 6
    
class Metro(VeiculoTransporte):
    def __init__(self, placa, capacidade_passageiros, consumo_energia_km):
        super().__init__(placa, capacidade_passageiros)
        self.consumo_energia_km = consumo_energia_km

    def calcularCustoOperacional(self):
        return self.consumo_energia_km * 0.80
    
def main():
    veiculos = []
    while True:
        print("\n===Menu===\n")
        print("1. Cadastrar ônibus.")
        print("2. Cadastrar metro.")
        print("3. Exibir custos operacionais.")
        print("4. Sair.")

        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            print("\nCadastro de ônibus.")
            try:
                placa = input("\nPlaca: ").strip()
                if placa == "":
                    raise ValueError("A placa não pode estar vazia.")
                
                capacidade = int(input("\nCapacidade de passageiros: "))
                if capacidade <= 0:
                    raise ValueError("Capacidade deve ser positiva.")
                
                consumo = float(input("\nConsumo por Km (litros/km): "))
                if consumo <= 0:
                    raise ValueError("Consumo deve ser positivo.")
                
                veiculos.append(Onibus(placa, capacidade, consumo))
                print("\nÔnibus cadastrado com sucesso.")
                
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            print("\nCadastro de metro.")
            try:
                placa = input("\nPlaca: ").strip()
                if placa == "":
                    raise ValueError("A placa não pode estar vazia.")
                
                capacidade = int(input("\nCapacidade de passageiros: "))
                if capacidade <= 0:
                    raise ValueError("Capacidade deve ser positiva.")
                
                consumo = float(input("\nConsumo de energia por Km (Kwh/km): "))
                if consumo <= 0:
                    raise ValueError("Consumo deve ser positivo.")
                
                veiculos.append(Metro(placa, capacidade, consumo))
                print("\nMetrô cadastrado com sucesso.")
                
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "3":
            if not veiculos:
                print("\nNenhum veículo cadastrado.\n")

            else:
                print("\n---Custos Operacionais por Km---")
                for v in veiculos:
                    tipo = "Ônibus" if isinstance(v, Onibus) else "Metrô"
                    custo = v.calcularCustoOperacional()
                    print(f"\n{tipo} - {v.placa}: R$ {custo:.2f} por Km")

        elif opcao == "4":
            print("\nEncerrando programa...\n")
            break

        else:
            print("\nOpção inválida. Escolha de 1-5.\n")

if __name__ == "__main__":
    main()