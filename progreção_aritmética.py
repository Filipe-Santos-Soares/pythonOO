class ProgreçãoAritimetica:
    def __init__(self, n, a1, r):
        self.n = n # Número de termos
        self.a1 = a1 # Primeiro termo
        self.r = r # Razão

    def gerar_termos(self):
        termos = []
        for i in range(self.n):
            termo = self.a1 + self.r * i 
            termos.append(termo)
        return termos
    
    def calcular_soma(self):
        an = self.a1 + self.r * (self.n - 1)
        soma = self.n * (self.a1 + an) / 2
        return soma

def main():
    print("\n====Progreção aritimética====\n")
    a1 = float(input("Digite o primeiro termo (a1): "))
    r = float(input("Digite a razão (r): "))
    n = int(input("Digite o número termos (n): "))

    pa = ProgreçãoAritimetica(n, a1, r)

    termos = pa.gerar_termos()
    print(f"\n Termos da PA: ")
    contador = 1
    for termo in termos:
        print(f"Termo {contador}: {termo}")
        contador += 1

    soma = pa.calcular_soma()
    print(f"\nSoma dos {n} termos: {soma}")
    



if __name__ =="__main__":
    main()