class Criptografador:
    def __init__(self, texto):
        self.texto = texto

    def substituir_vogais(self):
        #A – 4, E – 3, I – 1, O – 0, U – 8
        novo_texto = str.maketrans("aeiouAEIOU", "4310843108")
        return self.texto.translate(novo_texto)
    

def main():
    texto = input("\nDigite um texto: ")
    criptografia = Criptografador(texto)
    print(f"\nTexto criptografado: {criptografia.substituir_vogais()}")  


if __name__ =="__main__":
    main()