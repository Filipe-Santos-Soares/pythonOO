class LeitorDeStrings:
    def __init__(self, texto):
        self.texto = texto

    def numero_caracteres(self):
        return len(self.texto)

    def maiuscula(self):
        return self.texto.upper()

    def minuscula(self):
        return self.texto.lower()

    def contar_vogais(self):
        vogais = "aeiouAEIOU"
        contador = 0
        for caracter in self.texto:
            if caracter in vogais:
                contador += 1
        return contador

    def contem_ifb(self):
        return "IFB" in self.texto.upper()



def main():
    texto = input("\nDigite um texto: ")
    analisador = LeitorDeStrings(texto)

    print("\n===Analise de Texto===\n")
    print(f"\nNúmero de caractéres: {analisador.numero_caracteres()}")
    print(f"\nEm maiúsculas: {analisador.maiuscula()}")
    print(f"\nEm minúsculas: {analisador.minuscula()}")
    print(f"\nNúmero de vogais: {analisador.contar_vogais()}")
    if analisador.contem_ifb():
        print(f"\nA substring 'IFB' aparece no texto (independente de maiúsculas ou minúsculas).")
    else:
        print(f"\nA substring 'IFB' não aparece no texto.")
    



if __name__ =="__main__":
    main()